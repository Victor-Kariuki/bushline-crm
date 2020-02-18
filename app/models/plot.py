# app/models/plot.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db

class PlotStatus(enum.Enum):
    """
    plot status enum
    """

    sold = 'sold'
    booked = 'booked'
    available = 'available'


class Plot(db.Model):
    """
    Create a plot's table
    """

    __tablename__ = 'plots'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(60), nullable=False, index=True)
    description = db.Column(db.Text)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)
    estate_id = db.Column(db.Integer, db.ForeignKey('estates.id'))
    status = db.Column(db.Enum(PlotStatus), default='available')
    leads = db.relationship('Lead', backref='plot', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Plot: {}>'.format(self.name)