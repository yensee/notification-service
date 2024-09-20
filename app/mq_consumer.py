import pika
from app.mail_utils import send_email, send_sms

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue')

    def callback(ch, method, properties, body):
        event_data = body.decode('utf-8')
        print("Received notification event: {event_data}")
        if "email" in event_data:
            send_email("Notification", "recipient@example.com", f"Event: {event_data}")
        elif "sms" in event_data:
            send_sms("+1234567890", f"Event: {event_data}")

    channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for notification events...')
    channel.start_consuming()
