# app/lead/__init__.py

# 3rd party imports
from flask import Blueprint

lead = Blueprint('lead', __name__)

# local imports
from app.blueprints.lead import views
