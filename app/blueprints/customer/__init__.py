# app/blueprints/customer/__init__.py

# 3rd party imports
from flask import Blueprint

customer = Blueprint('customer', __name__)

# local imports
from app.blueprints.customer import views