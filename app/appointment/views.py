# app/appointment/views.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user

# local imports
from app import db
from app.appointment import appointment
from app.models import Appointment, User
from app.appointment.forms import AppointmentForm


def check_admin():
    if current_user.is_admin is False:
        abort(403)

@appointment.route('/')
@login_required
def read_appointments():
    """
    Handle requests to /appointments route
    Retrieve & render all appointments in the db
    """
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()

    return render_template('appointments/index.html.j2', appointments=appointments, title='appointments')


@appointment.route('/<int:id>')
@login_required
def read_appointment(id):
    """
    Handle requests to /appointments/<int:id> route
    Retrieve & render target appointment info
    """

    appointment = Appointment.query.filter_by(id=id).first()
    owner = User.query.filter_by(id=appointment.user_id).first()
    lead = Lead.query.filter_by(id=appointment.lead_id).first()

    return render_template('appointments/single.html.j2', appointment=appointment, owner=owner, lead=lead, title=appointment.name)


@appointment.route('/create', methods=['GET', 'POST'])
def create_appointment(id):
    """
    Handle requests to /appointments route
    Create & save a new appointment
    """

    form = appointmentForm()

    if form.validate_on_sumbit():

        appointment = appointment(
            title = form.title.data,
            description = form.description.data,
            date = form.date.data,
            lead_id = id,
            user_id = current_user.id
        )

        try:
            db.session.add(appointment)
            db.session.commit()

            flash('Successfully created the appointment.', 'info')

            return redirect(url_for('appointment.read_appointments', id=id))
        except:
            flash('Error creating the appointment', 'error')

    return render_template('appointments/form.html.j2', form=form, title='Create appointment')


@appointment.route('/update/<int:id>', methods=['GET', 'PUT'])
@login_required
def update_appointment(id):
    """
    Handle requests to /appointments/update/<int:id> route
    Update the target appointment
    """

    appointment = Appointment.query.get_or_404(id=id)

    form = appointmentForm(obj=appointment)

    if form.validate_on_submit():
        title = form.title.data,
        description = form.description.data,
        date = form.date.data
        
        try:
            db.session.add(appointment)
            db.session.commit()

            flash('Successfully updated the appointment', 'info')

            # redirect to the appointment's page
            return redirect(url_for('appointment.read_appointment', id=appointment.id))
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

    organization_id = appointment.organization_id

    db.session.delete(appointment)
    db.session.commit()

    flash('Successfully deleted the appointment')

    redirect(url_for('appointment.read_appointments', id=organization_id))
