# app/models/user.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# local imports
from app import db
from app.models.links import user_lead_links

class User(UserMixin, db.Model):
    """
    Create an User's table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True)
    avatar = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    customers = db.relationship('Customer', backref='user', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='user', lazy='dynamic')
    notes = db.relationship('Note', backref='user', lazy='dynamic')
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    leads = db.relationship('Lead', secondary=user_lead_links)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    update_on = db.Column(db.DateTime)

    def set_password(self, password):
        """
        Set password to hashed value
        """
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if password is hashed & matches user's input
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {}>'.format(self.email)

