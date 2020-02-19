# app/blueprints/inquiry/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

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