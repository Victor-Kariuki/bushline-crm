# app/models/plot.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db


class Status(enum.Enum):
    """
    plot status enum
    """

    sold = 'sold'
    booked = 'booked'
    available = 'available'


class Size(enum.Enum):
    """
    plot status enum
    """

    eighth = 'eighth'
    quarter = 'quarter'
    half = 'half'
    full = 'full'


class Plot(db.Model):
    """
    Create a plot's table
    """

    __tablename__ = 'plots'

    id = db.Column(db.Integer, primary_key=True)
    lr_number = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Enum(Size), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    status = db.Column(db.Enum(Status), default='available')
    clients = db.relationship('Client', backref='plot', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Plot: {}>'.format(self.lr_number)