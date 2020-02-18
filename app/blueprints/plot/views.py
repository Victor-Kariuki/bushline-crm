# app/plot/views.py

# inbuilt imports
import os

# 3rd party imports
from flask import render_template, url_for, redirect, flash, abort
from flask_login import current_user, login_required

# local imports
from app import db
from app.models import Plot
from app.blueprints.plot import plot
from app.blueprints.plot.forms import PlotForm


def check_admin():
    if current_user.is_admin is False:
        abort(403)


@plot.route('/')
@login_required
def read_plots():
    """
    Handle requests to /plots route
    Retrieve & render all plots in the db
    """

    plots = Plot.query.all()
    access_token = os.getenv('MAPBOX_ACCESS_TOKEN')

    return render_template('plots/index.html.j2', access_token=access_token, plots=plots, title='plots')


@plot.route('/<int:id>')
@login_required
def read_plot(id):
    """
    Handle requests to /plots/<int:id> route
    Retrieve & render target plot info
    """

    plot = Plot.query.get_or_404(id)

    access_token = os.getenv('MAPBOX_ACCESS_TOKEN')

    return render_template('plots/single.html.j2', access_token=access_token, plot=plot, title=plot.name)


@plot.route('/create', methods=['GET', 'POST'])
def create_plot():
    """
    Handle requests to /plots route
    Create & save a new plot
    """

    form = PlotForm()

    if form.validate_on_submit():

        plot = Plot(
            name = form.name.data,
            description = form.description.data,
            latitude = form.latitude.data,
            longitude = form.longitude.data,
            rating = form.rating.data,
            price = form.price.data,
            status = form.status.data,
            estate = form.data.estate
        )

        try:
            db.session.add(plot)
            db.session.commit()

            flash('Successfully created the Plot.', 'info')

            return redirect(url_for('plot.read_plots'))
        except:
            flash('Error creating the Plot', 'error')

    return render_template('plots/form.html.j2', form=form, title='Create Plot')


@plot.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_plot(id):
    """
    Handle requests to /plots/update/<int:id> route
    Update the target Plot
    """

    plot = Plot.query.get_or_404(id)

    form = PlotForm(obj=plot)

    if form.validate_on_submit():
        plot.name = form.name.data
        plot.description = form.description.data
        plot.latitude = form.latitude.data
        plot.longitude = form.longitude.data
        plot.rating = form.rating.data
        plot.price = form.price.data
        plot.status = form.status.data

        try:
            db.session.add(plot)
            db.session.commit()

            flash('Successfully updated the plot')
            # redirect to the Plot's page
            return redirect(url_for('plot.read_plot', id=plot.id))
        except:
            flash('Error updating the plot', 'error')

    return render_template('plots/form.html.j2', form=form, title='Update Plot')


@plot.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_plot(id):
    """
    Handle requests to /plots/delete/<int:id> route
    Delete the Plot
    """

    plot = Plot.query.get_or_404(id)

    try:
        db.session.delete(plot)
        db.session.commit()

        flash('Successfully deleted the plot', 'info')
    except:
        flash('Error deleting the plot', 'error')

    return redirect(url_for('plot.read_plots'))