# app/leads/views

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Lead, User
from app.lead import lead
from app.lead.forms import LeadForm


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

    return render_template('leads/single.html.j2', lead=lead, notes=notes, title=lead.first_name)


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
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            phone = form.phone.data,
            email = form.email.data,
            source = form.source.data,
            lead_type = form.lead_type.data,
            location = form.location.data,
            proposal = form.proposal.data,
            probability = form.probability.data,
            land_id = lead_json.get('land_id')[0],
            status = form.status.data
        )

        lead.assignees.append(form.user_id.data)

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
        lead_json = request.form.to_dict(flat=False)

        lead.first_name = form.first_name.data,
        lead.last_name = form.last_name.data,
        lead.phone = form.phone.data,
        lead.email = form.email.data,
        lead.source = form.source.data,
        lead.lead_type = form.lead_type.data,
        lead.status = form.status.data,
        location = form.location.data,
        lead.proposal = form.proposal.data,
        probability = form.probability.data,
        land_id = lead_json.get('land_id')[0]
        lead.assignees.append(form.user_id.data)

        # update the DB
        db.session.add(lead)
        db.session.commit()
        flash('You have successfully edited the lead.')

        # redirect to the leads page
        return redirect(url_for('lead.read_leads'))

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
