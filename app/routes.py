from flask import Blueprint, request, jsonify
from app.mail_utils import send_email, send_sms
from app.db.session import get_db

notification_bp = Blueprint('notification_bp', __name__)


@notification_bp.route('/notifications/send', methods=['POST'])
def send_notification():
    db = next(get_db())  # Get database session for MySQL

    # Simulate some database operation
    # Example: db.add() or db.query() for notifications

    data = request.json
    event_type = data.get('type')

    if event_type == 'email':
        send_email("Manual Notification", "recipient@example.com", "This is a test email.")
    elif event_type == 'sms':
        send_sms("+1234567890", "This is a test SMS.")

    return jsonify({"status": "Notification sent"})
