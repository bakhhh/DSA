#This code has been implemented based on LECTURE 2 pg18 COMP1002, Sem 2, 2022

class myException(Exception):
    pass

class valueError(myException):
    def __init__(self, message):
        self.message = message

class NotFoundError(myException):
    def __init__(self, message):
        self.message = message

class AlreadyEdge(myException):
    def __init__(self, message):
        self.message = message
