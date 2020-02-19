# app/blueprints/inquiry/views

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Inquiry, Note, Appointment, Task
from app.blueprints.inquiry import inquiry
from app.blueprints.inquiry.forms import InquiryForm, NoteForm, AppointmentForm, TaskForm


@inquiry.route('/')
@login_required
def read_inquiries():

    """
    Handles request to /inquiries route
    Retrieve & render all inquiries in the DB
    """

    inquiries = Inquiry.query.all()

    return render_template('inquiries/index.html.j2', inquiries=inquiries, title='Inquiries Listing')


@inquiry.route('/<int:id>')
@login_required
def read_inquiry(id):

    """
    Handles request to /inquiries/{id} route
    Retrieve & render target inquiry's details
    """

    inquiry = Inquiry.query.get_or_404(id)

    return render_template('inquiries/single.html.j2', inquiry=inquiry, title=inquiry.client.first_name)


@inquiry.route('/create', methods=['GET', 'POST'])
@login_required
def create_inquiry():
    """
    Handles requests to /inquiries/create route
    Create's a new inquiry
    """

    form = InquiryForm()

    if form.validate_on_submit():
        inquiry = Inquiry(
            title = form.title.data,
            proposal = form.proposal.data,
            probability = form.probability.data,
            source = form.source.data,
            client = form.client.data,
            plot = form.plot.data,
            user = form.user.data
        )

        try:
            db.session.add(inquiry)
            db.session.commit()
            flash('Successfully added the inquiry', 'info')

            # redirect to the inquiries page
            return redirect(url_for('inquiry.read_inquiries'))
        except:
            flash('Error creating the inquiry', 'error')

    # load inquiries template
    return render_template('inquiries/form.html.j2', form=form, title='Create inquiry')


@inquiry.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_inquiry(id):
    """
    Handles requests to /inquiries/update/{id} route
    Update the target user
    """

    inquiry = Inquiry.query.get_or_404(id)

    form = InquiryForm(obj=inquiry)

    if form.validate_on_submit():
        inquiry.proposal = form.proposal.data
        inquiry.probability = form.probability.data
        inquiry.source = form.source.data
        inquiry.plot = form.plot.data
        inquiry.client = form.client.data
        inquiry.user = form.user.data
        inquiry.updated_on = datetime.utcnow()

        try:
            # update the DB
            db.session.add(inquiry)
            db.session.commit()
            flash('You have successfully edited the inquiry.', 'info')

            # redirect to the inquiries page
            return redirect(url_for('inquiry.read_inquiry', id=id))
        except:
            flash('Error updating the inquiry', 'error')

    return render_template('inquiries/form.html.j2', form=form, title='Update inquiry')


@inquiry.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_inquiry(id):
    """
    Handles requests to /inquiries/delete/{id} route
    Delete an existing user
    """

    inquiry = Inquiry.query.get_or_404(id)

    # update the DB
    db.session.delete(inquiry)
    db.session.commit()
    flash('You have successfully deleted the inquiry.')

    # redirect to the inquiries page
    return redirect(url_for('inquiry.read_inquiries'))


@inquiry.route('/<int:id>/create-note', methods=['GET', 'POST'])
@login_required
def create_note(id):
    """
    Handle request to /inquiries/<id>/create-note route \n
    Create a new note and store in the DB
    """

    form = NoteForm()
    inquiry = Inquiry.query.get_or_404(id)

    if form.validate_on_submit():

        note = Note(
            title = form.title.data,
            description = form.description.data,
            inquiry = inquiry,
            user = current_user
        )

        try:
            db.session.add(note)
            db.session.commit()
            flash('You have successfully added a new note.', 'info')
            # redirect to the client's page
            return redirect(url_for('inquiry.read_inquiry', id=id))
        except:
            flash('Error creating the note', 'error')

    # load note form template
    return render_template('inquiries/note-form.html.j2', form=form, title='Add Note')


@inquiry.route('/<int:id>/create-appointment', methods=['GET', 'POST'])
def create_appointment(id):
    """
    Handle requests to /appointments route
    Create & save a new appointment
    """

    form = AppointmentForm()
    inquiry = Inquiry.query.get_or_404(id)

    if form.validate_on_submit():

        appointment = Appointment(
            title = form.title.data,
            description = form.description.data,
            date = form.date.data,
            time= form.time.data,
            client = inquiry.client,
            inquiry = inquiry,
            user = current_user
        )

        try:
            db.session.add(appointment)
            db.session.commit()

            flash('Successfully created the appointment.')

            return redirect(url_for('inquiry.read_inquiry', id=id))
        except:
            flash('Error creating the appointment')

    return render_template('inquiries/appointment-form.html.j2', form=form, title='Create appointment')


@inquiry.route('/<int:id>/create-task', methods=['GET', 'POST'])
@login_required
def create_task(id):
    """
    Handle requests to /inquiries/<int:id>/create-task route
    Create & save task
    """

    form = TaskForm()
    inquiry = Inquiry.query.get_or_404(id)

    if form.validate_on_submit():

        task = Task(
            title = form.title.data,
            description = form.description.data,
            start_date = form.start_date.data,
            end_date = form.end_date.data,
            status = form.status.data,
            inquiry = inquiry,
            user = current_user
        )

        try:
            db.session.add(task)
            db.session.commit()

            flash('Successfully created the task', 'info')

            return redirect(url_for('inquiry.read_inquiry', id=id))
        except:
            flash('Error creating the task', 'error')

    return render_template('inquiries/task-form.html.j2', form=form, title='Create Task')