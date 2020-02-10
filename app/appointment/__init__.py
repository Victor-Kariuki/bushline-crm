# app/appointment/__init__.py

# 3rd party imports
from flask import Blueprint

appointment = Blueprint('appointment', __name__)

# local imports
from app.appointment import views
