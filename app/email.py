# app/email.py

# 3rd party imports
from flask_mail import Message

# local imports
from app import mail

def send_mail(subject, sender, recipients, text_body, html_body):
    """Send email
    
    Arguments:
        subject {String} -- Mail's subject
        sender {String} -- Sender's email
        recipients {Array} -- List of recipients emails 
        text_body {String} -- Mail's message 
        html_body {File} -- HTML File
    """

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)