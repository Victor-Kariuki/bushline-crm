# app/lead/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email

# local imports
from app.models import User, Land
class LeadForm(FlaskForm):
    """
    Handle creation & updating of leads.
    """

    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone No')
    location = StringField('Location')
    proposal = StringField('Proposal')
    source = SelectField('Source', choices=[
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('whatsapp', 'whatsapp'),
        ('sms', 'sms'),
        ('call', 'call')
    ])
    lead_type = SelectField('Type', choices=[
        ('customer', 'customer'),
        ('new', 'new')
    ])
    land_id = QuerySelectField(query_factory=lambda: Land.query.all(), get_label="name")
    user_id = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
    status = SelectField('Status', choices=[
        ('active', 'active'),
        ('closed', 'closed'),
        ('lost', 'lost')
    ])
    probability = SelectField('Probability', choices=[
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    ])
    submit = SubmitField('Submit')
