# app/plot/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, NumberRange, Length


class ProjectForm(FlaskForm):
    """
    Form to handle creating & updating of project
    """

    name = StringField('Name', validators=[DataRequired()])
    latitude = StringField('Longitude')
    longitude = StringField('Longitude')
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Submit')


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
    submit = SubmitField('Submit')