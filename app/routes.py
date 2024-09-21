from flask import Blueprint, request, jsonify
from app.mail_utils import send_email, send_sms
from app.db.session import get_db
from app.models import Notification

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notifications/send', methods=['POST'])
def send_notification():
    db = next(get_db())  # Get the database session

    data = request.json
    event_type = data.get('type')
    recipient = data.get('recipient')  # Assuming recipient is in the request

    if event_type == 'email':
        message = data.get('message', 'This is a test email.')
        send_email("Notification", recipient, message)
        # send_email("Manual Notification", "recipient@example.com", "This is a test email.")
        # Persist notification in the database
        notification = Notification(recipient=recipient, message=message, notification_type='email', status='SENT')
        db.add(notification)
        db.commit()
    elif event_type == 'sms':
        message = data.get('message', 'This is a test SMS.')
        # send_sms("+1234567890", "This is a test SMS.")
        send_sms(recipient, message)
        # Persist notification in the database
        notification = Notification(recipient=recipient, message=message, notification_type='sms', status='SENT')
        db.add(notification)
        db.commit()

    return jsonify({"status": "Notification sent"})
#
# from flask import Blueprint, request, jsonify
# from app.mail_utils import send_email, send_sms
# from app.db.session import get_db
#
# notification_bp = Blueprint('notification_bp', __name__)
#
#
# @notification_bp.route('/notifications/send', methods=['POST'])
# def send_notification():
#     db = next(get_db())  # Get database session for MySQL
#
#     # Simulate some database operation
#     # Example: db.add() or db.query() for notifications
#
#     data = request.json
#     event_type = data.get('type')
#
#     if event_type == 'email':
#         send_email("Manual Notification", "recipient@example.com", "This is a test email.")
#     elif event_type == 'sms':
#         send_sms("+1234567890", "This is a test SMS.")
#
#     return jsonify({"status": "Notification sent"})
