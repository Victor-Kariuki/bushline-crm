# app/blueprint/project/__init__.py

# 3rd party imports
from flask import Blueprint

project = Blueprint('project', __name__)

# local imports
from app.blueprints.project import views