# app/task/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField
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
    status = SelectField('Status', choices=[
        ('pending', 'pending'),
        ('active', 'active'),
        ('closed', 'closed')
    ])
    lead_id = QuerySelectField(query_factory=lambda: Lead.query.all(), get_label="first_name")
    submit = SubmitField('submit')
