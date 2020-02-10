# app/models/note.py

# inbuilt imports
from datetime import datetime

# local imports
from app import db


class Note(db.Model):
    """
    Create a Note's table
    """

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime)

    def __repr__(self):
        return '<Note: {}>'.format(self.title)