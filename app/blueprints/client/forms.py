# app/blueprint/client/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Email


class ClientForm(FlaskForm):
    """
    Handle creation & updating of clients.
    """

    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    mobile = StringField('Mobile No', validators=[DataRequired()])
    tel = StringField('Tel')
    location = StringField('Location')
    submit = SubmitField('Submit')

