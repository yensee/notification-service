import json

from flask import Flask
from flask_mail import Message, Mail
import os
from app import Config

app = Flask(__name__)

# Configure Flask-Mail to use MailHog
app.config['MAIL_SERVER'] = Config.MAIL_SERVER
app.config['MAIL_PORT'] = Config.MAIL_PORT
app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = Config.MAIL_USE_SSL

# Initialize Flask-Mail
mail = Mail(app)

def save_email_locally(message):
    save_path = './saved_emails'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    email_file = os.path.join(save_path, f"{message.subject}.txt")
    with open(email_file, 'w') as f:
        f.write(f"To: {', '.join(message.recipients)}\n")
        f.write(f"Subject: {message.subject}\n")
        f.write(f"Body: {message.body}\n")
    print(f"Email saved to {email_file}")

def send_email(subject, recipient, body):
    email_body = json.dumps(body, indent=4)

    print(f"Email Body :  {email_body}")
    with app.app_context():

        msg = Message(subject, sender="no-reply@notifications.com", recipients=[recipient])
        msg.body = f"Here is your notification data:\n\n{email_body}"
        # For actual sending use mail.send(msg) in production
        # For saving locally in development or testing environment
        # save_email_locally(msg)
        mail.send(msg)

def send_sms(phone_number, message):
    # For offline mode, just print the SMS to console
    print(f"Simulated SMS to {phone_number}: {message}")
    with open("sms_log.txt", "a") as f:
        f.write(f"SMS to {phone_number}: {message}\n")