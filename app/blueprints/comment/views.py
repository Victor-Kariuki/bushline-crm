# app/blueprints/comment/views.py

# 3rd party imports
from flask import request, redirect, url_for, flash
from flask_login import current_user, login_required

# local imports
from app import db
from app.models import Comment
from app.blueprints.comment import comment


@comment.route('/<int:id>/create-note-comment', methods=['GET', 'POST'])
@login_required
def create_note_comment(id):
  """
  Handles requests to /comments/create route
  Create comments
  """

  return redirect(url_for('note.read_note', id=id))


@comment.route('/<int:id>/reply', methods=['GET', 'POST'])
@login_required
def create_reply(id):
  """
  Handles requests to /comments/<id>/create route
  Create comment reply
  """

  comment = Comment.query.get_or_404(id)

  

@comment.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_comment(id):
  """
  Handles requests to /comments/<id>/update route
  Update the target comment
  """

  comment = Comment.query.get_or_404(id)

  try:
    db.session.add(comment)
    db.session.commit()

    flash('Successfully updated comment.')
    return redirect(url_for('note.read_note', id=comment.note_id))
  except:
    flash('Error updating comment')


  return redirect(url_for('note.read_note', id=comment.note_id))


  
@comment.route('/<int:id>/delete-comment', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
  """
  Handles requests to /comments/<id>/delete route
  Delete the target comment
  """

  comment = Comment.query.get_or_404(id)

  try:
    db.session.delete(comment)
    db.session.commit()

    flash('Successfully deleted comment.')
  except:
    flash('Error deleting comment')
