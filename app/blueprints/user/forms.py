# app/user/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images


class UserForm(FlaskForm):
    """
    Form to handle creating & updating of an organization's users
    """

    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired()])
    avatar = FileField('Avatar', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('Submit')
