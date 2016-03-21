from Instructions import *

def init():
    declaration()
    affectation()
    name()
    value()
    add()
    sub()
    mul()
    div()
    
def declaration():
    def __go__(self):
        return self.tokens[1].__go__() + " := " + self.tokens[2].__go__()
    Declaration.__go__ = __go__

def affectation():
    def __go__(self):
        return self.tokens[0].__go__() + " = " + self.tokens[1].__go__()
    Affectation.__go__ = __go__

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

def sub():
    def __go__(self):
        return self.__str__()
    Sub.__go__ = __go__

def mul():
    def __go__(self):
        return self.__str__()
    Mul.__go__ = __go__

def div():
    def __go__(self):
        return self.__str__()
    Div.__go__ = __go__
