# app/user/views.py

# 3rd party imports
from flask import render_template, redirect, url_for, abort
from flask_login import current_user, login_required

# local imports
from app import db
from app.models import User
from app.blueprints.user import user
from app.blueprints.user.forms import UserForm

def check_admin():
    if current_user.is_admin is False:
        abort(403)


@user.route('/')
@login_required
def read_users():
    """
    Handle requests to /users route
    Retrieve & render all users in the db
    """

    users = User.query.all()

    return render_template('users/index.html.j2', users=users, title='users')

@user.route('/<int:id>')
@login_required
def read_user(id):
    """
    Handle requests to /user/<id> route
    Retrieve & render all user in the db
    """

    user = User.query.filter_by(id=id).all()

    return render_template('user/index.html.j2', user=user, title='Users')


@user.route('/update/<int:id>')
@login_required
def update_user(id):
    """
    Handle requests to /user/update/<int:id> route
    Update the target user
    """

    user = User.query.get_or_404(id=did)

    form = UserForm(obj=user)

    if form.validate_on_submit():
        user.username = form.username.data,
        user.first_name = form.first_name.data,
        user.last_name = form.last_name.data,
        user.email = form.email.data,
        user.phone = form.phone.data,

        db.session.add(user)
        db.session.commit()

        flash('Successfully updated your profile.')

        # redirect to the user's page
        return redirect(url_for('user.read_user', id=user.id))

    return render_template('user/form.html.j2', form=form, title='Update your profile')


@user.route('/user/delete/<int:id>')
@login_required
def delete_user(id):
    """
    Handle requests to /user/delete/<int:id> route
    Delete the user
    """

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    flash('Successfully deleted the user', 'info')

    return redirect(url_for('user.read_users'))