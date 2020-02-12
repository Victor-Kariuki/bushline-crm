# app/auth/views.py

# inbuilt imports
import os
from datetime import datetime

# 3rd party imports
from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from flask_mail import Message
from flask_dance.contrib.google import google

# local imports
from app import db, login_manager, mail
from app.blueprints.auth import auth
from app.blueprints.auth.forms import LoginForm, RegisterForm, ResetPasswordForm
from app.models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to /register route
    Add an user to the db through the registerform
    """


    form = RegisterForm()

    # POST: Handle user registration
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            phone = form.phone.data
        )

        # hash password
        user.set_password(form.password.data)

        try:
            # add user to the database
            db.session.add(user)
            db.session.commit()

            flash('You have successfully registered! You may now login.', 'info')

            # redirect to the login page
            return redirect(url_for('auth.login'))

        except:
            flash('Error creating account, please try again.', 'error')


    # GET: render register page template
    return render_template('auth/register.html.j2', form=form, title='Register')


@auth.route('')
def google_login():
    """Google Oauth redirect
    """

    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get("/plus/v1/people/me")
    if resp.ok: 
        resp_json = resp.json()
        print (resp_json)
        return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """

    form = LoginForm()

    # POST: Handle user authentication
    if form.validate_on_submit():
        # check if user exists in the db & the password matches
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):

            # log user in
            login_user(user)

            # redirect to the dashboard
            return redirect(url_for('lead.read_leads'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # GET: load login template
    return render_template('auth/login.html.j2', form=form, title='Login')


@auth.route('/reset-password', methods=['GET', 'PUT'])
@login_required
def reset_password():
    """
    Handle request to /reset-password routes
    Reset password
    """

    user = User.query.filter_by(id=current_user.id).first()

    form = ResetPasswordForm(obj=user)

    if form.validate_on_submit():

        user.set_password(form.password.data)
        user.updated_on = datetime.utcnow()

        db.session.add(user)
        db.session.commit()

        flash('Successfully reset password')

        return redirect(url_for('user.read_user', id=current_user.id))

    return render_template('auth/reset-password.html.j2', form=form, title='Reset Password')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))