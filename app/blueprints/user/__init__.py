# app/user/__init__.py

# 3rd party imports
from flask import Blueprint

user = Blueprint('user', __name__)

# local imports
from app.blueprints.user import views
