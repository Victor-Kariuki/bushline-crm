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
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.Enum(TaskStatus), default='active', nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    inquiry_id = db.Column(db.Integer, db.ForeignKey('inquiries.id'))
    comments = db.relationship('Comment', backref='task', lazy='dynamic')
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)


    def __repr__(self):
        return '<Task: {}>'.format(self.title)
