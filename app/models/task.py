# app/models/task.py

# inbuilt imports
import enum
from datetime import datetime

# local imports
from app import db


class TaskStatus(enum.Enum):
    """
    Task's enum
    """
    pending = 'pending'
    active = 'active'
    closed = 'closed'


class Task(db.Model):
    """
    Create task's table
    """

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable='False')
    description = db.Column(db.String(200))
    status = db.Column(db.Enum(TaskStatus), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))
    comments = db.relationship('Comment', backref='task', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    def __repr__(self):
        return '<Task: {}>'.format(self.title)
