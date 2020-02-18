# app/plot/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, NumberRange, Length

# import models
from app.models import Project

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
    status = SelectField('Status', choices=[
        ('sold', 'sold'),
        ('booked', 'booked'),
        ('available', 'available')
    ])
    project = QuerySelectField(query_factory=lambda: Project.query.all(), get_label="name")
    submit = SubmitField('Submit')