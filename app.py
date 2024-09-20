from app import create_app
from app.mq_consumer import consume_notifications
from threading import Thread

app = create_app()

if __name__ == "__main__":
    # Start RabbitMQ consumer in a separate thread
    Thread(target=consume_notifications).start()
    # Start Flask app
    app.run(port=5000)
