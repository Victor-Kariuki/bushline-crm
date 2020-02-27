# app/blueprints/dashboard/views.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask import render_template, url_for, redirect

# local imports
from app.blueprints.dashboard import dashboard

@dashboard.route('')
def index():
  """
  Handle requests to /dashboard route
  """
  return render_template('dashboard/index.html.j2', title='Dashboard')
