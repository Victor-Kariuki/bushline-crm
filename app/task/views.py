# app/task/views.py

# 3rd party imports
from flask import render_template, url_for, redirect, abort, flash
from flask_login import login_required, current_user

# local imports
from app import db
from app.models import Task, User, Lead
from app.task import task
from app.task.forms import TaskForm


@task.route('')
@login_required
def read_tasks():
    """
    Handle requests to /tasks route
    Retrieve & render all tasks in the db
    """

    if current_user.is_admin is False:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
    else:
        tasks = Task.query.all()

    return render_template('tasks/index.html.j2', tasks=tasks, title='tasks')


@task.route('/<int:id>')
@login_required
def read_task(id):
    """
    Handle requests to /tasks/<int:id> route
    Retrieve & render target task info
    """

    task = Task.query.filter_by(id=id).first()
    user = User.query.filter_by(id=task.user_id).first()
    lead = Lead.query.filter_by(id=task.lead_id).first()

    return render_template('tasks/single.html.j2', task=task, user=user, lead=lead, title=task.name)


@task.route('/create')
@login_required
def create_task():
    """
    Handle requests to /tasks route
    Create & save task
    """

    form = TaskForm()

    if form.validate_on_sumbit():

        task = Task(
            title = form.title.data,
            description = form.description.data,
            status = form.status.data,
            lead = form.lead.data,
            created_by = current_user.id
        )

        try:
            db.session.add(task)
            db.session.commit()

            flash('Successfully created the task', 'info')

            return redirect(url_for('task.read_tasks'))
        except:
            flash('Error creating the task', 'error')

    return render_template('tasks/form.html.j2', form=form, title='Create Task')


@task.route('/update/<int:id>')
@login_required
def update_task(id):
    """
    Handle requests to /tasks/update/<int:id> route
    Update the target task
    """

    task = Task.query.get_or_404(id=did)

    form = TaskForm(obj = task)

    if form.validate_on_submit():
        task.title = form.title.data,
        task.description = form.description.data,
        task.status = form.status.data,
        task.lead = form.lead.data,

        db.session.add(task)
        db.session.commit()

        flash('Successfully updated the task')

        # redirect to the task's page
        redirect(url_for('task.read_task', id=task.id))

    return render_template('tasks/form.html.j2', form=form, title='Update Task')


@task.route('/delete/<int:id>')
@login_required
def delete_task(id):
    """
    Handle requests to /tasks/delete/<int:id> route
    Remove the target task
    """

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    flash('Successfully deleted the task')

    redirect(url_for(task.read_tasks))