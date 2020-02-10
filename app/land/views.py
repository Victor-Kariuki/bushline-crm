# app/land/views.py

# 3rd party imports
from flask import render_template, url_for, redirect, flash, abort
from flask_login import current_user, login_required

# local imports
from app import db
from app.models import Land
from app.land import land
from app.land.forms import LandForm


def check_admin():
    if current_user.is_admin is False:
        abort(403)


@land.route('/')
@login_required
def read_lands():
    """
    Handle requests to /lands route
    Retrieve & render all lands in the db
    """

    lands = Land.query.all()

    return render_template('lands/index.html.j2', lands=lands, title='lands')


@land.route('/<int:id>')
@login_required
def read_land(id):
    """
    Handle requests to /lands/<int:id> route
    Retrieve & render target land info
    """

    land = Land.query.get_or_404(id)

    return render_template('lands/single.html.j2', land=land, title=land.name)


@land.route('/create', methods=['GET', 'POST'])
def create_land():
    """
    Handle requests to /lands route
    Create & save a new land
    """

    form = LandForm()

    if form.validate_on_submit():

        land = Land(
            name = form.name.data,
            description = form.description.data,
            location = form.location.name,
            rating = form.rating.data,
            price = form.price.data,
            status = form.status.data,
        )

        try:
            db.session.add(land)
            db.session.commit()

            flash('Successfully created the Land.', 'info')

            return redirect(url_for('land.read_lands'))
        except:
            flash('Error creating the Land', 'error')

    return render_template('lands/form.html.j2', form=form, title='Create Land')


@land.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_land(id):
    """
    Handle requests to /lands/update/<int:id> route
    Update the target Land
    """

    land = Land.query.get_or_404(id=id)

    form = LandForm(obj=Land)

    if form.validate_on_submit():
        land.name = form.name.data,
        land.description = form.description.data,
        land.rating = form.rating.data,
        land.price = form.price.data,
        land.status = form.status.data

        try:
            db.session.add(land)
            db.session.commit()

            flash('Successfully updated the land')
            # redirect to the Land's page
            return redirect(url_for('land.read_Land', id=land.id))
        except:
            flash('Error updating the land', 'error')

    return render_template('lands/form.html.j2', form=form, title='Update Land')


@land.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_land(id):
    """
    Handle requests to /lands/delete/<int:id> route
    Delete the Land
    """

    land = Land.query.get_or_404(id)

    try:
        db.session.delete(land)
        db.session.commit()

        flash('Successfully deleted the land', 'info')
    except:
        flash('Error deleting the land', 'error')

    return redirect(url_for('land.read_lands'))