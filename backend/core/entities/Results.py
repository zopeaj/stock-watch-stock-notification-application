class Result:
    def __init__(self, success, message, data):
        self.success = success
        self.message = message
        self.data = data

    def getMessage(self):
        return self.message

    def isSuccess(self):
        return self.success

    def getData(self):
        return self.data
