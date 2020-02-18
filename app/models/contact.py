# app/models/contact.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db

class Contact(db.Model):
    """
    Create a contact's table
    """

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(128), unique=True)
    website = db.Column(db.String(128), unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Contact: {}>'.format(self.email)