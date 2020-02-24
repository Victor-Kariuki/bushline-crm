# app/blueprints/client/views

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Client, Inquiry
from app.blueprints.client import client
from app.blueprints.client.forms import ClientForm, InquiryForm


@client.route('/leads')
@login_required
def read_leads():

    """
    Handles request to /clients/leads route
    Retrieve & render all leads in the DB
    """

    if current_user.is_admin == True:
        leads = Client.query.filter_by(type='lead').all()
    else:
        leads = Client.query.filter_by(type='lead', added_by=current_user.id).all()

    return render_template('clients/leads.html.j2', leads=leads, title='Leads Listing')


@client.route('/customers')
@login_required
def read_customers():

    """
    Handles request to /clients/customers route
    Retrieve & render all customers in the DB
    """

    if current_user.is_admin == True:
        customers = Client.query.filter_by(type='customer').all()
    else:
        customers = Client.query.filter_by(type='customer', added_by=current_user.id).all()

    return render_template('clients/customers.html.j2', customers=customers, title='Customers Listing')


@client.route('/<int:id>')
@login_required
def read_client(id):

    """
    Handles request to /clients/{id} route
    Retrieve & render target client's details
    """

    client = Client.query.filter_by(id=id).first_or_404()

    return render_template('clients/single.html.j2', client=client, title=client.first_name)


@client.route('/create', methods=['GET', 'POST'])
@login_required
def create_client():
    """
    Handles requests to /clients/create route
    Create's a new client
    """

    form = ClientForm()

    if form.validate_on_submit():
        client = Client(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            mobile = form.mobile.data,
            location = form.location.data,
            user = current_user
        )

        try:
            db.session.add(client)
            db.session.commit()
            flash('Successfully added the client', 'info')

            # redirect to the clients page
            return redirect(url_for('client.read_leads'))
        except:
            flash('Error creating the client', 'error')

    # load clients template
    return render_template('clients/form.html.j2', form=form, title='Create Lead')


@client.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_client(id):
    """
    Handles requests to /clients/update/{id} route
    Update the target user
    """

    client = Client.query.get_or_404(id)

    form = ClientForm(obj=client)

    if form.validate_on_submit():
        client.first_name = form.first_name.data
        client.last_name = form.last_name.data
        client.email = form.email.data
        client.mobile = form.mobile.data
        client.location = form.location.data
        client.updated_on = datetime.utcnow()

        try:
            # update the DB
            db.session.add(client)
            db.session.commit()
            flash('You have successfully edited the client.', 'info')

            # redirect to the clients page
            return redirect(url_for('client.read_client', id=id))
        except:
            flash('Error updating the client', 'error')

    return render_template('clients/form.html.j2', form=form, title='Update client')


@client.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_client(id):
    """
    Handles requests to /clients/delete/{id} route
    Delete an existing user
    """

    client = Client.query.get_or_404(id)

    # update the DB
    db.session.delete(client)
    db.session.commit()
    flash('You have successfully deleted the client.')

    # redirect to the clients page
    return redirect(url_for('client.read_clients'))


@client.route('/<int:id>/create-inquiry', methods=['GET', 'POST'])
def create_inquiry(id):
    """
    Handles requests to /clients/id/create-inquiry route
    Delete an existing user
    """

    form = InquiryForm()

    client = Client.query.get_or_404(id)

    if form.validate_on_submit():
        inquiry = Inquiry(
            proposal = form.proposal.data,
            probability = form.probability.data,
            source = form.source.data,
            client = client,
            plot = form.plot.data,
            user = form.user.data
        )

        try:
            db.session.add(inquiry)
            db.session.commit()
            flash('You have successfully added a new inquiry.', 'nfo')

            # redirect to the inquirys page
            return redirect(url_for('client.read_client',id=id))
        except:
            flash('Error creating the inquiry', 'error')

    return render_template('clients/inquiry-form.html.j2', form=form, title='Create Inquiry')



