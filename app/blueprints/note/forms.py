# app/notes/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from app.models import Client, Appointment

class NoteForm(FlaskForm):
    """
    Handle creation & updating of appointment notes.
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    appointment =  QuerySelectField(query_factory=lambda: Appointment.query.all(), get_label="title")
    client = QuerySelectField(query_factory=lambda: Client.query.all(), get_label="first_name")
    submit = SubmitField('Submit')
