# app/appointment/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class AppointmentForm(FlaskForm):
    """
    Form to handle creating & updating of appointments
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    date = DateField('Date', format='%m/%d/%Y')
    submit = SubmitField('Submit')