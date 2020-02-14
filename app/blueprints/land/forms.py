# app/land/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, NumberRange, Length


class LandForm(FlaskForm):
    """
    Form to handle creating & updating of lands
    """

    name = StringField('Name', validators=[DataRequired()])
    latitude = StringField('Longitude')
    longitude = StringField('Longitude')
    description = TextAreaField('Description', validators=[Length(max=200)])
    rating = RadioField('Rating', choices = [('1','1'),('2','2'), ('3','3'),('4','4'),('5', '5')])
    price = IntegerField('Price', validators=[NumberRange(min=10000)])
    status = SelectField('Status', choices=[
        ('sold', 'sold'),
        ('booked', 'booked'),
        ('available', 'available')
    ])
    submit = SubmitField('Submit')