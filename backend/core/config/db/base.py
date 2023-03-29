import os, sys
from dotenv import load_dotenv
path = os.environ['FILE_PATH']
sys.path.append(path)

from db.base_class import Base
