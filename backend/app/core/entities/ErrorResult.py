import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from backend.core.entities.Results import Result

class ErrorResults(Result):
    def __init__(self, message, data):
        super().__init__(False, message, data)


