# app/leads/views

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Lead, User, Appointment, Note
from app.blueprints.lead import lead
from app.blueprints.lead.forms import LeadForm, AppointmentForm, NoteForm


@lead.route('')
@login_required
def read_leads():

    """
    Handles request to /leads route
    Retrieve & render all leads in the DB
    """

    leads = Lead.query.all()

    return render_template('leads/index.html.j2', leads=leads, title='leads')


@lead.route('/<int:id>')
@login_required
def read_lead(id):

    """
    List all leads
    """

    lead = Lead.query.filter_by(id=id).first()

    notes = Note.query.filter_by(lead_id=id).all()

    return render_template('leads/single.html.j2', lead=lead, notes=notes, title=lead.customer.first_name)


@lead.route('/create', methods=['GET', 'POST'])
@login_required
def create_lead():
    """
    Handles requests to /leads/create route
    Create a new lead
    """

    form = LeadForm()

    if form.validate_on_submit():
        lead = Lead(
            customer = form.customer.data,
            source = form.source.data,
            proposal = form.proposal.data,
            probability = form.probability.data,
            land = form.land.data
        )

        lead.assignees.append(form.user.data)

        try:
            db.session.add(lead)
            db.session.commit()
            flash('You have successfully added a new lead.', 'info')

            # redirect to the leads page
            return redirect(url_for('lead.read_leads'))
        except:
            flash('Error creating the lead', 'error')

    # load leads template
    return render_template('leads/form.html.j2', form=form, title='Add lead')


@lead.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_lead(id):
    """
    Edit the lead
    """
    lead = Lead.query.get_or_404(id)
    form = LeadForm(obj=lead)

    if form.validate_on_submit():
        lead.assignees.append(form.user.data)
        lead.customer = form.customer.data,
        lead.source = form.source.data,
        lead.proposal = form.proposal.data,
        lead.probability = form.probability.data,
        lead.land = form.land.data
        lead.updated_on = datetime.utcnow()
        
        try:
            # update the DB
            db.session.add(lead)
            db.session.commit()
            flash('You have successfully edited the lead.', 'info')

            # redirect to the leads page
            return redirect(url_for('lead.read_leads'))
        except:
            flash('Error updating the lead', 'error')

    return render_template('leads/form.html.j2', form=form, title='Update lead')


@lead.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_lead(id):
    """
    Delete a lead from the DB
    """

    lead = Lead.query.get_or_404(id)

    # update the DB
    db.session.delete(lead)
    db.session.commit()
    flash('You have successfully deleted the lead.')

    # redirect to the leads page
    return redirect(url_for('lead.read_leads'))


@lead.route('/<int:id>/create-note', methods=['GET', 'POST'])
def create_note(id):
    """
    Handle request to /leads/<id>/create note route
    Create a new note for the lead
    """

    form = NoteForm()

    lead = Lead.query.get_or_404(id)

    if form.validate_on_submit():
        note = Note(
            title = form.title.data,
            description = form.description.data,
            lead = lead,
            user = current_user
        )

        try:
            # update the DB
            db.session.add(note)
            db.session.commit()
            flash('Successfully added a new note.', 'info')

            # redirect to the leads page
            return redirect(url_for('lead.read_lead', id=id))
        except:
            flash('Error updating the lead', 'error')
    
    return render_template('leads/note-form.html.j2', form=form, title='Create Note')
