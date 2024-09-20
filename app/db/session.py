from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# MySQL connection URL - use environment variables to configure
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/notification_service")

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

# Dependency to get DB session in FastAPI/Flask views
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
