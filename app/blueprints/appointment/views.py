# app/appointment/views.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, redirect, url_for, abort, flash, jsonify
from flask_login import login_required, current_user

# local imports
from app import db
from app.blueprints.appointment import appointment
from app.models import Appointment, User, Client, Inquiry
from app.blueprints.appointment.forms import AppointmentForm


@appointment.route('/')
@login_required
def read_appointments():
    """
    Handle requests to /appointments route
    Retrieve & render all appointments in the db
    """
    if current_user.is_admin is False:
        appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    else:
        appointments = Appointment.query.all()
    

    return render_template('appointments/index.html.j2', appointments=appointments, title='appointments')


@appointment.route('/<int:id>')
@login_required
def read_appointment(id):
    """
    Handle requests to /appointments/<int:id> route
    Retrieve & render target appointment info
    """

    appointment = Appointment.query.get_or_404(id)

    return render_template('appointments/single.html.j2', appointment=appointment, title=appointment.name)


@appointment.route('/create', methods=['GET', 'POST'])
def create_appointment():
    """
    Handle requests to /appointments route
    Create & save a new appointment
    """

    form = AppointmentForm()

    if form.validate_on_submit():

        appointment = Appointment(
            title = form.title.data,
            description = form.description.data,
            location = form.location.data,
            start = form.start.data,
            client = form.client.data,
            user = current_user
        )

        try:
            db.session.add(appointment)
            db.session.commit()

            flash('Successfully created the appointment.')

            return redirect(url_for('appointment.read_appointments'))
        except:
            flash('Error creating the appointment')

    return render_template('appointments/form.html.j2', form=form, title='Create appointment')


@appointment.route('/update/<int:id>', methods=['GET', 'PUT'])
@login_required
def update_appointment(id):
    """
    Handle requests to /appointments/update/<int:id> route
    Update the target appointment
    """

    appointment = Appointment.query.get_or_404(id=id)

    form = AppointmentForm(obj=appointment)

    if form.validate_on_submit():
        appointment.title = form.title.data
        appointment.description = form.description.data
        appointment.start = form.start.data,
        appointment.location = form.location.data,
        appointment.client = form.client.data,
        appointment.inquiry = form.inquiry.data,
        
        try:
            db.session.add(appointment)
            db.session.commit()

            flash('Successfully updated the appointment', 'info')

            # redirect to the appointment's page
            return redirect(url_for('appointment.read_appointment', id=id))
        except:
            flash('Error updating the appointment', 'error')

    return render_template('appointments/form.html.j2', form=form, title='Update appointment')


@appointment.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_appointment(id):
    """
    Handle requests to /appointments/delete/<int:id> route
    Delete the appointment
    """

    appointment = Appointment.query.get_or_404(id)

    db.session.delete(appointment)
    db.session.commit()

    flash('Successfully deleted the appointment')

    redirect(url_for('appointment.read_appointments'))
