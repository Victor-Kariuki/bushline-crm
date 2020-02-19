# app/blueprints/dashboard/views.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, url_for, redirect

# local imports
from app.models import User, client, Client, Plot, Inquiry
from app.blueprints.dashboard import dashboard

@dashboard.route('')
def index():
  """
  Handle requests to /dashboard route
  """

  clients = Client.query.all()
  users = User.query.all()
  plots = Plot.query.all()
  clients = client.query.all()

  return render_template('dashboard/index.html.j2', clients=clients, users=users, plots=plots, title='Dashboard')