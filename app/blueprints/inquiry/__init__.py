# app/blueprints/inquiry/__init__.py

# 3rd party imports
from flask import Blueprint

inquiry = Blueprint('inquiry', __name__)

# local imports
from app.blueprints.inquiry import views