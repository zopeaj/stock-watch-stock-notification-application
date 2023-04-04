import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.modules.stock.models import Stock
from backend.core.config.db.get_db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

class StockRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, stock):
        pass

    def update(self, stock_id, stock):
        pass

    def delete(self, stock_id):
        pass

    def getById(self, stock_id):
        pass
