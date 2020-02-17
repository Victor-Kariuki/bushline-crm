# app/auth/__init__.py

# inbuilt imports
import os

# 3rd party imports
from flask import Blueprint

auth = Blueprint('auth', __name__)

# local imports
from app.blueprints.auth import views
