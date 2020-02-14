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
    phone = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    leads = db.relationship('Lead', backref='customer', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='customer', lazy='dynamic')
    comments = db.relationship('Comment', backref='customer', lazy='dynamic')
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Customer: {}>'.format(self.email)