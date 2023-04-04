import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.modules.notification.models import Notification
from backend.modules.notification.repository import NotificationRepository

class NotificationService:
    def __init__(self, notificationRepository):
        self.notificationRepository = notificationRepository



