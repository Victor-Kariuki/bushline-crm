# app/models/links.py

# local imports
from app import db

user_inquiry_links = db.Table('user_inquiry_links',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('inquiry_id', db.Integer, db.ForeignKey('inquiries.id'))
)
