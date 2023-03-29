import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.core.entities.Results import Result

class SuccessResult(Result):
    def __init__(self, sucess, message, data):
        super().__init__(True, message, data)

