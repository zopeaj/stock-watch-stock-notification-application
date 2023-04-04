import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.modules.notification.models import Notification
from backend.core.config.db.get_db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


class NotificationRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, notification):
        pass

    def update(self, notification_id, notification):
        pass

    def getById(self, notification_id):
        pass

    def delete(self, notification_id):
        pass

