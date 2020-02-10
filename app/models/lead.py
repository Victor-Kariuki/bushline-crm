# app/models.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db
from app.models.links import user_lead_links

class Source(enum.Enum):
    """
    Lead sources enum
    """

    facebook = 'facebook'
    twitter = 'twitter'
    whatsapp = 'whatsapp'
    sms = 'sms'
    call = 'call'


class LeadType(enum.Enum):
    """
    Lead types enum
    """

    customer = 'customer'
    new = 'new'


class Status(enum.Enum):
    """
    Lead status enum
    """

    active = 'active'
    closed = 'closed'
    lost = 'lost'


class Probability(enum.Enum):
    """
    Lead status enum
    """

    high = 'high'
    medium = 'medium'
    low = 'low'


class Lead(db.Model):
    """
    Create a Lead's table
    """

    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    phone = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    source = db.Column(db.Enum(Source))
    lead_type = db.Column(db.Enum(LeadType))
    location = db.Column(db.String(60), nullable=False)
    proposal = db.Column(db.Integer)
    probability = db.Column(db.Enum(Probability))
    land_id = db.Column(db.Integer, db.ForeignKey('lands.id'))
    status = db.Column(db.Enum(Status))
    assignees = db.relationship('User', secondary=user_lead_links)
    appointments = db.relationship('Appointment', backref='lead', lazy='dynamic')
    comments = db.relationship('Comment', backref='lead', lazy='dynamic')
    tasks = db.relationship('Task', backref='lead', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Lead: {}>'.format(self.email)