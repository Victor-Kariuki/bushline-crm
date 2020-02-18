# app/models/project.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db


class Project(db.Model):
    """
    Create a project's table
    """

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    plots = db.relationship('Plot', backref='project', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Project: {}>'.format(self.name)