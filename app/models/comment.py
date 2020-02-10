# app/models/comment.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db

class Comment(db.Model):
    """
    Create comment's table
    """

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Comment: {}>'.format(self.comment)
