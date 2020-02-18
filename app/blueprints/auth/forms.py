# app/blueprint/auth/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

# local imports
from app.models import User


class RegisterForm(FlaskForm):
    """
    Form for users to create a new account.
    """

    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone No', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('register')

    def validate_email(self, email):
        """
        validate email
        """
        employee = User.query.filter_by(email = email.data).first()
        if employee is not None:
            raise ValidationError('Please use a different email.')


class LoginForm(FlaskForm):
    """
    Form to authenticate existing users.
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')


class ResetPasswordForm(FlaskForm):
    """
    Form to update existing employee's password
    """

    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password'), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('reset password')
