# app/auth/__init__.py

# 3rd party imports
from flask import Blueprint

auth = Blueprint('auth', __name__)

# local imports
from app.auth import views
