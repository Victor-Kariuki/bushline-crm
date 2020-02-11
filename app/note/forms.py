# app/notes/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from app.models import Lead

class NoteForm(FlaskForm):
    """
    Handle creation & updating of appointment notes.
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    lead_id = QuerySelectField(query_factory=lambda: Lead.query.all(), get_label="first_name")
    submit = SubmitField('Submit')
