# app/models/land.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db

class LandStatus(enum.Enum):
    """
    Land status enum
    """

    sold = 'sold'
    booked = 'booked'
    available = 'available'


class Land(db.Model):
    """
    Create a land's table
    """

    __tablename__ = 'lands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, index=True)
    description = db.Column(db.Text)
    location = db.Column(db.String(64))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)
    status = db.Column(db.Enum(LandStatus))
    leads = db.relationship('Lead', backref='land', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Land: {}>'.format(self.name)