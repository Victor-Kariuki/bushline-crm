# app/blueprint/appointment/forms.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_components import DateRange, TimeField
from wtforms.validators import DataRequired, Length

# local imports
from app.models import Inquiry, Client


class AppointmentForm(FlaskForm):
    """
    Form to handle creating & updating of appointments
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    date = DateField('Date')
    time = TimeField('Time')
    inquiry = QuerySelectField(query_factory=lambda: Inquiry.query.all(), get_label="client.first_name")
    client = QuerySelectField(query_factory=lambda: Client.query.all(), get_label="first_name")
    submit = SubmitField('Submit')