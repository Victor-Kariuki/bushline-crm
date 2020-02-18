# app/blueprints/client/__init__.py

# 3rd party imports
from flask import Blueprint

client = Blueprint('client', __name__)

# local imports
from app.blueprints.client import views