# app/models/inquiry.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db
from app.models.links import user_inquiry_links


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


class Status(enum.Enum):
    """
    Inquiry status enum
    """

    active = 'active'
    closed = 'closed'
    lost = 'lost'


class Probability(enum.Enum):
    """
    Inquiry status enum
    """

    high = 'high'
    medium = 'medium'
    low = 'low'


class Inquiry(db.Model):
    """
    Create a Inquiry's table
    """

    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False, index=True)
    proposal = db.Column(db.Integer)
    probability = db.Column(db.Enum(Probability))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    plot_id = db.Column(db.Integer, db.ForeignKey('plots.id'))
    status = db.Column(db.Enum(Status), default='active')
    source = db.Column(db.Enum(Source), nullable=False)
    assignees = db.relationship('User', secondary=user_inquiry_links, backref='inquiry', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='inquiry', lazy='dynamic')
    notes = db.relationship('Note', backref='inquiry', lazy='dynamic')
    comments = db.relationship('Comment', backref='inquiry', lazy='dynamic')
    tasks = db.relationship('Task', backref='inquiry', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Inquiry: {}>'.format(self.title)