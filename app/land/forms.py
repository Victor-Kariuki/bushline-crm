# app/land/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length


class LandForm(FlaskForm):
    """
    Form to handle creating & updating of lands
    """

    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    rating = IntegerField('Rating', validators=[NumberRange(min=0, max=10)])
    price = IntegerField('Price', validators=[NumberRange(min=10000)])
    status = SelectField('Status', choices=[
        ('sold', 'sold'),
        ('booked', 'booked'),
        ('available', 'available')
    ])
    submit = SubmitField('Submit')