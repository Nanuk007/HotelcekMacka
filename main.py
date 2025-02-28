
from flask import Flask
from flask import render_template, url_for, redirect, request, flash
from flask_login import LoginManager, login_user, login_required
from forms import RegistrationForm, AdminForm
from models import db, User , Admin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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

@app.route('/')
def home():
    return render_template('index.html')

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
            flash('Vošiel si', "success")
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
        flash('Reservation successful!', 'success')
        return redirect(url_for('register'))
    return render_template('roomselect.html', form=form)


with app.app_context():
    db.create_all()

