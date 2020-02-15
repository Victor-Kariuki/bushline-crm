# app/blueprints/dashboard/__init__.py

# 3rd party imports
from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

# local imports
from app.blueprints.dashboard import views