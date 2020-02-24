# app/blueprint/client/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email

# local imports
from app.models import Plot, User, Client


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


class InquiryForm(FlaskForm):
  """
  Handles creating & updating of inquiries
  """

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
  user = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
  submit = SubmitField('Submit')