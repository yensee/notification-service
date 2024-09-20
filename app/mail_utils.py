from flask_mail import Message
from app import mail
import os

def save_email_locally(message):
    save_path = './saved_emails'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    email_file = os.path.join(save_path, f"{message.subject}.txt")
    with open(email_file, 'w') as f:
        f.write("To: {', '.join(message.recipients)}\n")
        f.write("Subject: {message.subject}\n")
        f.write("Body: {message.body}\n")
    print(f"Email saved to {email_file}")

def send_email(subject, recipient, body):
    msg = Message(subject, sender="no-reply@notifications.com", recipients=[recipient])
    msg.body = body
    # Save emails locally in offline mode
    save_email_locally(msg)

def send_sms(phone_number, message):
    print(f"Simulated SMS to {phone_number}: {message}")
    with open("sms_log.txt", "a") as f:
        f.write(f"SMS to {phone_number}: {message}\n")
