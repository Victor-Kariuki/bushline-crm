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

    customer = 'customer'
    lead = 'lead'
    

class Source(enum.Enum):
    """
    Client sources enum
    """

    facebook = 'facebook'
    twitter = 'twitter'
    whatsapp = 'whatsapp'
    sms = 'sms'
    call = 'call'
    mail = 'mail'


class Client(db.Model):
    """
    Create a clients' table
    """

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    tel = db.Column(db.Integer, unique=True)
    location = db.Column(db.String(60), nullable=False)
    source = db.Column(db.Enum(Source), nullable=False)
    type = db.Column(db.Enum(Type), default='lead', nullable=False)
    inquiries = db.relationship('Inquiry', backref='client', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='client', lazy='dynamic')
    is_blacklisted = db.Column(db.Boolean, default=False)
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullabe=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Customer: {}>'.format(self.email)