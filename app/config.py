import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'

    # Flask-Mail settings
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_SUPPRESS_SEND = True  # To simulate sending emails locally
    MAIL_SAVE_PATH = './saved_emails'

    # RabbitMQ settings (if using RabbitMQ)
    RABBITMQ_URL = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')

    # Database settings
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///notification_service.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
