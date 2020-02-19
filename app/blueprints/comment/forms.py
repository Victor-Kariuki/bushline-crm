# app/blueprints/comment/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
  """
  Handles creating & updating of comments
  """

  comment = TextAreaField('Comment', validators=[DataRequired()])
  submit = SubmitField('Submit')