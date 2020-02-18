# app/blueprints/customer/views

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Customer, Lead, Contact
from app.blueprints.customer import customer
from app.blueprints.customer.forms import CustomerForm, LeadForm, ContactForm


@customer.route('')
@login_required
def read_customers():

    """
    Handles request to /customers route
    Retrieve & render all customers in the DB
    """

    customers = Customer.query.all()

    return render_template('customers/index.html.j2', customers=customers, title='customers')


@customer.route('/<int:id>')
@login_required
def read_customer(id):

    """
    List all customers
    """

    customer = Customer.query.filter_by(id=id).first()

    return render_template('customers/single.html.j2', customer=customer, title=customer.first_name)


@customer.route('/create', methods=['GET', 'POST'])
@login_required
def create_customer():
    """
    Handles requests to /customers/create route
    Create a new customer
    """

    form = CustomerForm()

    if form.validate_on_submit():
        customer = Customer(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            phone = form.phone.data,
            email = form.email.data,
            location = form.location.data,
            user = current_user
        )

        try:
            db.session.add(customer)
            db.session.commit()
            flash('You have successfully added a new customer.', 'info')

            # redirect to the customers page
            return redirect(url_for('customer.read_customers'))
        except:
            flash('Error creating the customer', 'error')

    # load customers template
    return render_template('customers/form.html.j2', form=form, title='Add customer')


@customer.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_customer(id):
    """
    Handles requests to /customers/update/id route
    Update the target user
    """
    customer = Customer.query.get_or_404(id)
    form = CustomerForm(obj=customer)

    if form.validate_on_submit():
        customer.first_name = form.first_name.data
        customer.last_name = form.last_name.data
        customer.phone = form.phone.data
        customer.email = form.email.data
        customer.location = form.location.data
        customer.updated_on = datetime.utcnow()

        try:
            # update the DB
            db.session.add(customer)
            db.session.commit()
            flash('You have successfully edited the customer.', 'info')

            # redirect to the customers page
            return redirect(url_for('customer.read_customer', id=customer.id))
        except:
            flash('Error updating the customer', 'error')

    return render_template('customers/form.html.j2', form=form, title='Update customer')


@customer.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_customer(id):
    """
    Handles requests to /customers/delete/id route
    Delete an existing user
    """

    customer = Customer.query.get_or_404(id)

    # update the DB
    db.session.delete(customer)
    db.session.commit()
    flash('You have successfully deleted the customer.')

    # redirect to the customers page
    return redirect(url_for('customer.read_customers'))


@customer.route('/<int:id>/create-lead', methods=['GET', 'POST'])
def create_lead(id):
    """
    Handles requests to /customers/id/create-lead route
    Delete an existing user
    """

    form = LeadForm()

    customer = Customer.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():
        lead = Lead(
            source = form.source.data,
            proposal = form.proposal.data,
            probability = form.probability.data,
            customer = customer,
            plot = form.plot.data
        )

        lead.assignees.append(form.user.data)

        try:
            db.session.add(lead)
            db.session.commit()
            flash('You have successfully added a new lead.', 'nfo')

            # redirect to the leads page
            return redirect(url_for('customer.read_customer',id=id))
        except:
            flash('Error creating the lead', 'error')

    return render_template('customers/lead-form.html.j2', form=form, title='Create Lead')


@customer.route('/<int:id>/add-contact', methods=['GET', 'POST'])
def add_contact(id):
    """
    Handles requests to /customers/<id>/add_contact route
    add new contact info for the customer
    """

    form = ContactForm()
    customer = Customer.query.get_or_404(id)

    if form.validate_on_submit():
        contact = Contact(
            phone = form.phone.data,
            email = form.email.data,
            website = form.website.data,
            customer = customer
        )

        try:
            db.session.add(contact)
            db.session.commit()

            flash('successfully added new contact info', 'info')
            return redirect(url_for('customer.read_customer', id=id))
        except:
            flash('Error creating confact info')

    return render_template('customers/contact-form.html.j2', form=form, title='Add Contact Info')
