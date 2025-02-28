from flask import Flask
from flask import render_template, url_for, redirect, request, flash
from flask_login import LoginManager
from forms import PridajClanokFormular
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from forms import RegistrationForm, LoginForm
from models import Clanok, db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clanky.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = 'tvoj_krastny_sigma_klucik'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roomselect')
def roomselect():
    return render_template('roomselect.html')

@app.route('/onas')
def onas():
    return render_template('onas.html')

@app.route('/adminLog')
def admin():
    return render_template('admin-log.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email už existuje', 'error')
            return redirect(url_for('register'))

        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrovaný úspešne!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Prihlásenie úspešné', 'success')
            return redirect(url_for('home'))
        else:
            flash('Nesprávny email alebo heslo', 'error')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Úspešne ste sa odhlásili!', 'success')
    return redirect(url_for('login'))

with app.app_context():
    db.create_all()