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

    proposal = StringField('Proposal')
    source = SelectField('Source', choices=[
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('whatsapp', 'whatsapp'),
        ('sms', 'sms'),
        ('call', 'call')
    ])
    land_id = QuerySelectField(query_factory=lambda: Land.query.all(), get_label="name")
    user_id = QuerySelectField(query_factory=lambda: User.query.all(), get_label="username")
    probability = SelectField('Probability', choices=[
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    ])
    submit = SubmitField('Submit')
