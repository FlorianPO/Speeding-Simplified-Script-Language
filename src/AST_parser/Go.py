from Instructions import *

def init():
    declaration()
    name()
    value()
    add()
    
def declaration():
    def __go__(self):
        return self.tokens[1].__go__() + " := " + self.tokens[2].__go__()
    Declaration.__go__ = __go__

def name():
    def __go__(self):
        return self.__str__()
    Name.__go__ = __go__

def value():
    def __go__(self):
        return self.__str__()
    Value.__go__ = __go__

def add():
    def __go__(self):
        return self.__str__()
    Add.__go__ = __go__
