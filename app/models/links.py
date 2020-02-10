# app/models/links.py

# local imports
from app import db

user_lead_links = db.Table('user_lead_links',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('lead_id', db.Integer, db.ForeignKey('leads.id'))
)
