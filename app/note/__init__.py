# app/note/__init__.py

# 3rd party imports
from flask import Blueprint

note = Blueprint('note', __name__)

# local imports
from app.note import views
