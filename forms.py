from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    cat_name = StringField('Cat\'s Name', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    from_date = DateField('From Date', format='%Y-%m-%d', validators=[DataRequired()])
    to_date = DateField('To Date', format='%Y-%m-%d', validators=[DataRequired()])

    # 20 rooms to choose from
    room = SelectField('Select Room', 
                       choices=[(f'Room {i}', f'Room {i}') for i in range(1, 21)], 
                       validators=[DataRequired()])

    submit = SubmitField('Register')

class AdminForm(FlaskForm):
    AID = PasswordField('Admin ID', validators=[DataRequired()])  # Using AdminID as password
    submit = SubmitField('Login')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    review = TextAreaField('Review', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Submit')