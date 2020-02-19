# app/blueprints/inquiry/forms.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_components import DateRange, TimeField
from wtforms.validators import DataRequired, Length

# local imports
from app.models import Plot, User, Client


class InquiryForm(FlaskForm):
  """
  Handles creating & updating of inquiries
  """

  title = StringField('Title')
  plot = QuerySelectField(query_factory=lambda: Plot.query.all(), get_label="lr_number")
  source = SelectField('Source', choices=[
    ('facebook', 'facebook'),
    ('twitter', 'twitter'),
    ('whatsapp', 'whatsapp'),
    ('sms', 'sms'),
    ('call', 'call'),
    ('mail', 'mail')
  ])
  proposal = StringField('Proposal')
  probability = SelectField('Probability', choices=[
    ('high', 'high'),
    ('medium', 'medium'),
    ('low', 'low')
  ])
  client = QuerySelectField(query_factory=lambda: Client.query.all(), get_label="first_name")
  user = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
  submit = SubmitField('Submit')


class NoteForm(FlaskForm):
    """
    Handle creation & updating of appointment notes.
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AppointmentForm(FlaskForm):
    """
    Form to handle creating & updating of appointments
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time')
    submit = SubmitField('Submit')


class TaskForm(FlaskForm):
    """
    Form to handle creating & updating tasks
    """

    description = TextAreaField('Description', validators=[Length(max=200)])
    start_date = DateField('Start Date')
    end_date = DateField('End Date')
    status = SelectField('Status', choices=[
        ('pending', 'pending'),
        ('active', 'active'),
        ('closed', 'closed')
    ])
    submit = SubmitField('submit')