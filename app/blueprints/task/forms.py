# app/task/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

# local imports
from app.models import Lead


class TaskForm(FlaskForm):
    """
    Form to handle creating & updating tasks
    """

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=200)])
    start_date = DateField('Start Date', format='%m/%d/%Y')
    end_date = DateField('End Date', format='%m/%d/%Y')
    status = SelectField('Status', choices=[
        ('pending', 'pending'),
        ('active', 'active'),
        ('closed', 'closed')
    ])
    lead = QuerySelectField(query_factory=lambda: Lead.query.all(), get_label="customer")
    submit = SubmitField('submit')
