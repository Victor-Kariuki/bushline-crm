# app/models/appointment.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db

class Appointment(db.Model):
    """
    Create an Appointment's table
    """

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text)
    start = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    inquiry_id = db.Column(db.Integer, db.ForeignKey('inquiries.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    notes = db.relationship('Note', backref='appointment', lazy='dynamic')
    comments = db.relationship('Comment', backref='appointment', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Appointment: {}>'.format(self.title)
