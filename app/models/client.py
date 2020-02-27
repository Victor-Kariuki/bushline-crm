# app/models/client.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db


class Type(enum.Enum):
    """
    Client types enum
    """

    client = 'client'
    lead = 'lead'


class Client(db.Model):
    """
    Create a clients' table
    """

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), unique=True)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    type = db.Column(db.Enum(Type), default='lead', nullable=False)
    inquiries = db.relationship('Inquiry', backref='client', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='client', lazy='dynamic')
    is_blacklisted = db.Column(db.Boolean, default=False)
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<client: {}>'.format(self.email)
