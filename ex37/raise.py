class MyException(BaseException):
    def __init__(self):
        self.message = "boom"

try:
    raise MyException()
except MyException, e: 
    print e.message



