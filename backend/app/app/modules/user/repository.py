import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.modules.user.models import User
from backend.core.config.db.get_db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

class UserRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, user):
        pass

    def update(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def getById(self, user_id):
        pass
