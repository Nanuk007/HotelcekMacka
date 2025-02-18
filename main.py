from flask import Flask
from flask import render_template, url_for, redirect, request, flash
# from flask_login import LoginManager
# from forms import PridajClanokFormular
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
# from forms import RegistrationForm, LoginForm
# from models import Clanok, db, User

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clanky.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

app.secret_key = 'macak'

@app.route('/')
def home():
    flash('toto je skuska')
    return render_template('index.html')

# @app.route('/clanky')
# def clanky():
#     cl = Clanok.query.all()
#     return render_template('clanky.html', clanky=cl)

# @app.route('/onas')
# def onas():
#     return render_template('onas.html')

# @app.route('/profil')
# def profil():
#     return render_template('profil.html')

# @app.route('/pridaj_clanok', methods=['POST', 'GET'])
# def pridaj_clanok():
#     f = PridajClanokFormular()
#     print('idzem')
#     print(f.validate_on_submit())
#     if f.validate_on_submit():
#         print('aj tu idzem')
#         nc = Clanok(nazov=f.titulka.data, obsah=f.obsah.data)
#         db.session.add(nc)
#         db.session.commit()
#         return redirect(url_for('clanky'))
#     return render_template('pridaj_clanok.html', form = f)

# @app.template_filter('shorten')
# def shorten_text(text, length=100):
#     if len(text) > length:
#         return text[:length] + '...'  # Skrátenie a pridanie trojbodky
#     return text

# @app.route('/clanok/<int:id>')
# def detail_clanku(id):
#     # Načítanie článku podľa ID
#     clanok = Clanok.query.get_or_404(id)
#     return render_template('clanok.html', clanok=clanok)

# @app.route('/upravit_clanok/<int:clanok_id>', methods=['GET', 'POST'])
# def upravit_clanok(clanok_id):
#     clanok = Clanok.query.get_or_404(clanok_id)  # Načítanie článku podľa ID
#     form = PridajClanokFormular()  # Tento formulár môže byť rovnaký ako na pridanie článku

#     # Predvyplnenie formuláru s existujúcimi hodnotami článku
#     if request.method == 'GET':
#         form.titulka.data = clanok.nazov
#         form.obsah.data = clanok.obsah

#     if form.validate_on_submit():  # Ak formulár bol odoslaný
#         clanok.nazov = form.titulka.data  # Aktualizácia názvu
#         clanok.obsah = form.obsah.data    # Aktualizácia obsahu
#         db.session.commit()  # Uloženie zmien do databázy
#         return redirect(url_for('clanky'))  # Presmerovanie na zoznam článkov

#     return render_template('uprav_clanok.html', form=form, clanok=clanok)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
#             flash('Email už existuje')
#             return redirect(url_for('register'))

#         new_user = User(username=form.username.data, email=form.email.data)
#         new_user.set_password(form.password.data)
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Registrovaný úspešne!')
#         return redirect(url_for('login'))

#     return render_template('register.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.check_password(form.password.data):
#             flash('Prihlásenie úspešné')
#             return redirect(url_for('home'))
#         else:
#             flash('Nesprávny email alebo heslo')

#     return render_template('login.html', form=form)

# with app.app_context():
#     db.create_all()