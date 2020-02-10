# app/land/__init__.py

# 3rd party imports
from flask import Blueprint

land = Blueprint('land', __name__)

# local imports
from app.land import views