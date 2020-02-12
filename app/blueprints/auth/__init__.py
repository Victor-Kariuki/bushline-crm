# app/auth/__init__.py

# inbuilt imports
import os

# 3rd party imports
from flask import Blueprint
from flask_dance.contrib.google import make_google_blueprint

auth = Blueprint('auth', __name__)
google_bp = make_google_blueprint(
    client_id = os.getenv('GOOGLE_CLIENT_ID'),
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET'),
)

# local imports
from app.blueprints.auth import views
