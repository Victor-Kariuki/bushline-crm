# app/plot/__init__.py

# 3rd party imports
from flask import Blueprint

plot = Blueprint('plot', __name__)

# local imports
from app.blueprints.plot import views