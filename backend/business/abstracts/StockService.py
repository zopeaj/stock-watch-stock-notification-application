import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.modules.stock.models import Stock
from backend.modules.stock.repository import StockRepository
