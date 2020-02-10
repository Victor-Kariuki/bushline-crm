# app/notes/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    """
    Handle creation & updating of appointment notes.
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Submit')
