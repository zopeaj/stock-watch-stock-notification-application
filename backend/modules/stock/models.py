import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from sqlalchemy import Column, String
from backend.core.config.db.base import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default='')
