from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

# class PridajClanokFormular(FlaskForm):
#     titulka = StringField('Názov článku', validators=[DataRequired()])
#     obsah = TextAreaField('Obsah článku', validators=[DataRequired()])
#     odoslat = SubmitField('Pridaj článok')

# class RegistrationForm(FlaskForm):
#     username = StringField('Používateľské meno', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Heslo', validators=[DataRequired()])
#     password_confirm = PasswordField('Potvrďte heslo', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Registrovať')

class AdminLog(FlaskForm):
    adminID = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    submit = SubmitField('Log In')