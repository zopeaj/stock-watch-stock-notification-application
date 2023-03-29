import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from sqlalchemy import Column, String, Integer, ForeignKey
from backend.core.config.db.base import Base

class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False, default='message')
    reasons = Column(String, nullable=False, default='')
    user = Column(ForeignKey("user.id"), backref="notification")

