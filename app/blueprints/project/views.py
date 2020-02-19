# app/blueprint/project/views.py

# inbuilt imports
import os
from datetime import datetime

# 3rd party imports
from flask import render_template, url_for, redirect, flash, abort
from flask_login import current_user, login_required

# local imports
from app import db
from app.models import Project, Plot
from app.blueprints.project import project
from app.blueprints.project.forms import ProjectForm, PlotForm


def check_admin():
    if current_user.is_admin is False:
        abort(403)


@project.route('/')
@login_required
def read_projects():
    """
    Handle requests to /projects route
    Retrieve & render all projects in the db
    """

    projects = Project.query.all()
    access_token = os.getenv('MAPBOX_ACCESS_TOKEN')

    return render_template('projects/index.html.j2', access_token=access_token, projects=projects, title='projects')


@project.route('/<int:id>')
@login_required
def read_project(id):
    """
    Handle requests to /projects/<int:id> route
    Retrieve & render target project info
    """

    project = Project.query.get_or_404(id)

    access_token = os.getenv('MAPBOX_ACCESS_TOKEN')

    return render_template('projects/single.html.j2', access_token=access_token, project=project, title=project.name)


@project.route('/create', methods=['GET', 'POST'])
def create_project():
    """
    Handle requests to /projects route
    Create & save a new project
    """

    form = ProjectForm()

    if form.validate_on_submit():

        project = Project(
            name = form.name.data,
            description = form.description.data,
            latitude = form.latitude.data,
            longitude = form.longitude.data,
        )

        try:
            db.session.add(project)
            db.session.commit()

            flash('Successfully created the Project.')
            return redirect(url_for('project.read_projects'))
        except:
            flash('Error creating the Project')

    return render_template('projects/form.html.j2', form=form, title='Create Project')


@project.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_project(id):
    """
    Handle requests to /projects/update/<int:id> route
    Update the target Project
    """

    project = Project.query.get_or_404(id)

    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.latitude = form.latitude.data
        project.longitude = form.longitude.data
        project.updated_on = datetime.utcnow()

        try:
            db.session.add(project)
            db.session.commit()

            flash('Successfully updated the project')
            # redirect to the Project's page
            return redirect(url_for('project.read_project', id=project.id))
        except:
            flash('Error updating the project', 'error')

    return render_template('projects/form.html.j2', form=form, title='Update Project')


@project.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    """
    Handle requests to /projects/delete/<int:id> route
    Delete the Project
    """

    project = Project.query.get_or_404(id)

    try:
        db.session.delete(project)
        db.session.commit()

        flash('Successfully deleted the project', 'info')
    except:
        flash('Error deleting the project', 'error')

    return redirect(url_for('project.read_projects'))


@project.route('/<int:id>/add-plot', methods=['GET', 'POST'])
@login_required
def add_plot(id):
    """
    Handle requests to /projects/<int:id>/add-plot route
    Add a route to the project
    """

    form = PlotForm()
    project = Project.query.get_or_404(id)

    if form.validate_on_submit():

        plot = Plot(
            lr_number = form.lr_number.data,
            description = form.description.data,
            latitude = form.latitude.data,
            longitude = form.longitude.data,
            size = form.size.data,
            price = form.price.data,
            project = project
        )

        try:
            db.session.add(plot)
            db.session.commit()

            flash('Successfully created the plot.', 'info')

            return redirect(url_for('project.read_project', id=id))
        except:
            flash('Error creating the Plot', 'error')

    return render_template('projects/plot-form.html.j2', form=form, title='Create Plot')