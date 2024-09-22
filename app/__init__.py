from flask import Flask
from flask_mail import Mail
from app.config import Config
from app.db.session import engine
from app.models import Base

app = Flask(__name__)



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Create the database tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Register routes
    from app.routes import notification_bp
    app.register_blueprint(notification_bp)

    return app
