# app/__init__.py

# local imports
import os

# 3rd party imports
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# DB Variable init
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)
    login_manager.init_app(app)

    # config flask_login
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app=app, db=db)

    # import all db models
    from app.models import Comment, Plot, Lead, Note, Task, User, Appointment, Project, Contact

    # import & register blueprints
    from app.blueprints.appointment import appointment as appointment_blueprint
    app.register_blueprint(appointment_blueprint, url_prefix='/appointments')

    from app.blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.blueprints.customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint, url_prefix='/customers')

    from app.blueprints.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from app.blueprints.project import project as project_blueprint
    app.register_blueprint(project_blueprint, url_prefix='/projects')

    from app.blueprints.plot import plot as plot_blueprint
    app.register_blueprint(plot_blueprint, url_prefix='/plots')

    from app.blueprints.lead import lead as lead_blueprint
    app.register_blueprint(lead_blueprint, url_prefix='/leads')

    from app.blueprints.note import note as note_blueprint
    app.register_blueprint(note_blueprint, url_prefix='/notes')

    from app.blueprints.task import task as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/tasks')

    from app.blueprints.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')

    # redirect to register on a fresh instance
    @app.route('/')
    def index():
        return redirect(url_for('auth.register'))

    # error handlers
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html.j2', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html.j2', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html.j2', title='Server Error'), 500

    return app

