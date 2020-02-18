# app/models/customer.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db


class Customer(db.Model):
    """
    Create a customers's table
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), unique=True)
    phone = db.Column(db.Integer, unique=True)
    location = db.Column(db.String(60), nullable=False)
    contacts = db.relationship('Contact', backref='customer', lazy='dynamic')
    leads = db.relationship('Lead', backref='customer', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='customer', lazy='dynamic')
    comments = db.relationship('Comment', backref='customer', lazy='dynamic')
    is_blacklisted = db.Column(db.Boolean, default=False)
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Customer: {}>'.format(self.email)