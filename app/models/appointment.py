# app/models/appointments.py

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
    description = db.Column(db.String(200))
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment', backref='appointment', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Appointment: {}>'.format(self.title)