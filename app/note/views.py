# app/note/views

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Note, Lead
from app.note import note
from app.note.forms import NoteForm

@note.route('/')
@login_required
def read_notes():
    """
    Handle request to /notes route \n
    Retrieve and render all notes
    """

    if current.is_admin is False:
        notes = Note.query.filter_by(created_by=current_user.id).all()
    else:
        notes = Note.query.all()

    return render_template('notes/index.html.j2', title='Notes')

@note.route('/create', methods=['GET', 'POST'])
@login_required
def create_note():
    """
    Handle request to /notes/create route \n
    Create a new note and store in the DB
    """

    form = NoteForm()

    if form.validate_on_submit():

        note = Note(
            title = form.title.data,
            description = form.description.data,
            created_by = current_user.id
        )

        try:
            db.session.add(note)
            db.session.commit()
            flash('You have successfully added a new note.', 'info')
            # redirect to the lead's page
            return redirect(url_for('note.read_notes'))
        except:
            flash('Error creating the note', 'error')

    # load note form template
    return render_template('notes/form.html.j2', form=form, title='Add Note')


@note.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_note(id):
    """
    Handles request to the /notes/update/<int:id> route
    Update's the target note
    """

    note = Note.query.get_or_404(id)
    
    form = NoteForm(obj=note)

    if form.validate_on_submit():
        title = form.title.data,
        description = form.description.data,

        # update the note's instance in the DB
        db.session.add(note)
        db.session.commit()
        flash('You have successfully edited the note.')

        # redirect to the lead's page
        return redirect(url_for('note.read_note', id=note.id))

    return render_template('notes/form.html.j2', form=form, title='Update Note')


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

    # redirect to the lead's page
    return redirect(url_for('note.read_notes'))
