# app/note/views

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Note
from app.blueprints.note import note
from app.blueprints.note.forms import NoteForm
from app.blueprints.comment.forms import CommentForm


@note.route('/')
@login_required
def read_notes():
    """
    Handle request to /notes route \n
    Retrieve and render all notes
    """

    if current_user.is_admin is False:
        notes = Note.query.filter_by(created_by=current_user.id).all()
    else:
        notes = Note.query.all()

    return render_template('notes/index.html.j2', notes=notes, title='Notes')


@note.route('/<int:id>', methods=['GET', 'POST'])
@login_required
def read_note(id):
    """
    Handle request to /notes route \n
    Retrieve and render all notes
    """

    note = Note.query.get_or_404(id)
    form = CommentForm()

    return render_template('notes/single.html.j2', note=note, form=form, title='Notes')


@note.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_note(id):
    """
    Handle request to /inquiries/<id>/update route \n
    Udpate the target note
    """


    note = Note.query.get_or_404(id)
    form = NoteForm(obj=note)

    if form.validate_on_submit():

        note.title = form.title.data
        note.description = form.description.data
        note.updated_on = datetime.utcnow()

        try:
            db.session.add(note)
            db.session.commit()
            flash('You have successfully added a new note.', 'info')
            # redirect to the client's page
            return redirect(url_for('inquiry.read_inquiry', id=id))
        except:
            flash('Error creating the note', 'error')

    # load note form template
    return render_template('note/form.html.j2', form=form, title='Update Note')



@note.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_note(id):
    """
    Handles request to the /notes/delete/<int:id> route
    Delete's the target note
    """

    note = Note.query.get_or_404(id)

    # Delete the note's instance on the DB
    db.session.delete(note)
    db.session.commit()
    flash('You have successfully deleted the note.')

    # redirect to the client's page
    return redirect(url_for('note.read_notes'))

