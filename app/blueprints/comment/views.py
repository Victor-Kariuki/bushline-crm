# app/blueprints/comment/views.py

# 3rd party imports
from flask import request, redirect, url_for

# local imports
from app.models import Comment
from app.blueprints.comment import comment


@comment.route('/<int:id>/create-note-comment', methods=['GET', 'POST'])
def create_note_comment(id):
  """
  Handles requests to /comments/create route
  Create comments
  """

  

  return redirect(url_for('note.read_note', id=id))