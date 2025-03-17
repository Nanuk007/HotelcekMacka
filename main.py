from flask import Flask, render_template, url_for, redirect, request, flash, Response
from flask_login import LoginManager, login_user, login_required
from forms import RegistrationForm, AdminForm, EmailForm
from models import db, User, Admin, EmailReview
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import send_file
import io

app = Flask(__name__)

# Configuring the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotelcek.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



app.secret_key = 'tvoj_krastny_sigma_klucik'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader 
def load_user(user_id):
    # Check both User and Admin tables
    user = User.query.get(int(user_id))
    if user:
        return user
    
    admin = Admin.query.get(int(user_id))
    return admin  # Returns Admin if found, otherwise None

@app.route('/', methods=['GET', 'POST'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        new_review = EmailReview(email=form.email.data, review=form.review.data)
        db.session.add(new_review)
        db.session.commit()
        flash('Vaša Review bola odoslaná a spokojne "ignorovaná"', 'success')  # Flash message

        return redirect(url_for('home'))  # Redirect to clear form after submission

    return render_template('index.html', form=form)  # No reviews passed


@app.route('/adminview')
@login_required
def adminview():
    return render_template('adminview.html')

@app.route('/adminLog', methods=['GET', 'POST'])  
def admin():
    form = AdminForm()
    if form.validate_on_submit():  
        # Fetch the admin by AID (Admin ID)
        admin = Admin.query.filter_by(AID=form.AID.data).first()  

        if admin:
            # Check if the admin ID matches (here, you're directly comparing AID, no need to hash)
            login_user(admin)
            flash('Vošiel si do macacej rite', "success")
            return redirect(url_for('adminview'))
        else:
            flash('ZLÉ ADMIN ID', 'error')  # Incorrect Admin ID

    return render_template('adminLog.html', form=form)

@app.route('/roomselect', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            cat_name=form.cat_name.data,
            telephone=form.telephone.data,
            email=form.email.data,
            room=form.room.data,
            from_date=form.from_date.data,
            to_date=form.to_date.data
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Regular flash message for reservation success
        flash('Vymňauknuté', 'success')

        # Important flash message asking about the PDF generation
        flash('Chcete PDF fakturku', 'info')

        return redirect(url_for('register'))
    
    return render_template('roomselect.html', form=form)

@app.route('/generate_pdf', methods=['GET', 'POST'])
def generate_pdf():
    # Retrieve the most recent reservation (last added user)
    latest_user = User.query.order_by(User.id.desc()).first()  # Get the most recent user

    if latest_user:
        # Create a PDF in memory using reportlab
        pdf_file = io.BytesIO()
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Write the PDF content (custom message + reservation details)
        c.drawString(100, 750, f"Milá/ý pán/i {latest_user.first_name} {latest_user.last_name},")
        c.drawString(100, 735, "dovolujeme si vám oznámit, že vaša rezervácia bola zaevidovaná v systéme.")
        c.drawString(100, 720, "P.S. nechat nám ju tu nafurt. HMMMMMMMMMM?")

        # Save the PDF to the in-memory file
        c.save()

        # Go to the beginning of the BytesIO buffer
        pdf_file.seek(0)

        # Send the generated PDF file to the user as a downloadable response
        return send_file(pdf_file, as_attachment=True, download_name="reservation.pdf", mimetype="application/pdf")
    else:
        flash("No reservations found.", "error")
        return redirect(url_for('home'))
    

with app.app_context():
    db.create_all()

