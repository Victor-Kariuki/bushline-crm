# app/lead/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email

# local imports
from app.models import User, plot, Customer
class LeadForm(FlaskForm):
    """
    Handle creation & updating of leads.
    """

    customer = QuerySelectField(query_factory=lambda: Customer.query.all(), get_label="first_name")
    proposal = StringField('Proposal')
    source = SelectField('Source', choices=[
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('whatsapp', 'whatsapp'),
        ('sms', 'sms'),
        ('call', 'call')
    ])
    plot = QuerySelectField(query_factory=lambda: plot.query.all(), get_label="name")
    user = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
    probability = SelectField('Probability', choices=[
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    ])
    submit = SubmitField('Submit')


class NoteForm(FlaskForm):
    """
    Handle creation of new notes for the lead
    """
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AppointmentForm(FlaskForm):
    """
    Handle creation of new appoitments for the lead
    """


class ReassignForm(FlaskForm):
    """
    Handle assiging of a lead new appoitments for the lead
    """

    user = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
    submit = SubmitField('Submit')