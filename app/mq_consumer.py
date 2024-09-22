import json

import pika
from app.mail_utils import send_email, send_sms

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue')

    def callback(ch, method, properties, body):
        event_data_str = body.decode('utf-8')

        event_data = json.loads(event_data_str)

        channel_type = event_data['type']
        recipient = event_data['recipient']
        # message = event_data['message']
        # status = event_data['status']

        print(f"Received notification event: {event_data}")

        if channel_type == 'email':
            send_email("Notification", recipient, event_data)
        elif channel_type == 'sms':
            send_sms("+1234567890", f"Event: {event_data}")

    channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for notification events...')
    channel.start_consuming()
