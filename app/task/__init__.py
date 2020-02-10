# app/task/__init__.py

# 3rd party imports
from flask import Blueprint

task = Blueprint('task', __name__)

# local imports
from app.task import views