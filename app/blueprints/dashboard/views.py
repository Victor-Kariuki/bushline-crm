# app/blueprints/dashboard/views.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, url_for, redirect

# local imports
from app.models import User, Customer, Lead, Land
from app.blueprints.dashboard import dashboard

@dashboard.route('')
def index():
  """
  Handle requests to /dashboard route
  """

  leads = Lead.query.all()
  users = User.query.all()
  lands = Land.query.all()
  customers = Customer.query.all()

  return render_template('dashboard/index.html.j2', leads=leads, users=users, lands=lands, customers=customers, title='Dashboard')