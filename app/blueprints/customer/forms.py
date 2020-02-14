# app/lead/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Email

# local imports
from app.models import User, Land
class LeadForm(FlaskForm):
    """
    Handle creation & updating of leads.
    """

    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone No')
    location = StringField('Location')
    submit = SubmitField('Submit')
