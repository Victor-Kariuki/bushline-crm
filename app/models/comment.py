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
    comment = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    inquiry_id = db.Column(db.Integer, db.ForeignKey('inquiries.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Comment: {}>'.format(self.comment)
