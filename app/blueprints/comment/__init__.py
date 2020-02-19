# app/blueprints/comment/__init.py

#3rd party imports
from flask import Blueprint

comment = Blueprint('comment', __name__)

# local imports
from app.blueprints.comment import views