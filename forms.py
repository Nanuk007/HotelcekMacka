from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Používateľské meno', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    password_confirm = PasswordField('Potvrďte heslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrovať')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    submit = SubmitField('Prihlásiť sa')