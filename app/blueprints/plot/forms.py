# app/plot/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, NumberRange, Length

# import models
from app.models import Project, Client, User

class PlotForm(FlaskForm):
    """
    Form to handle creating & updating of plots
    """

    lr_number = StringField('LR Number', validators=[DataRequired()])
    latitude = StringField('Longitude')
    longitude = StringField('Longitude')
    description = TextAreaField('Description', validators=[Length(max=200)])
    size = SelectField('Size', choices=[
        ('eighth', 'eighth'),
        ('quarter', 'quarter'),
        ('half', 'half'),
        ('full', 'full')
    ])
    price = IntegerField('Price', validators=[NumberRange(min=10000)])
    project = QuerySelectField(query_factory=lambda: Project.query.all(), get_label="name")
    submit = SubmitField('Submit')


class InquiryForm(FlaskForm):
  """
  Handles creating & updating of inquiries
  """

  title = StringField('Title')
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
  assignee = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
  submit = SubmitField('Submit')
