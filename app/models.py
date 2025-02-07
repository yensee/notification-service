from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base
from datetime import datetime

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)
    notification_type = Column(String(6), nullable=False)  # 'email' or 'sms'
    status = Column(String(6), default="SENT")  # SENT, FAILED
    timestamp = Column(DateTime, default=datetime.utcnow)
