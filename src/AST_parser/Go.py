from Nodes.Instruction import *
from Nodes.Expression import *
from Nodes.Function import *
from Nodes.Operator import *
from Nodes.Block import *

def init():
    declaration()
    declaffectation()
    affectation()
    
    functiondef()
    functioncall()
    arguments()
    parameters()
    block()

    name()
    value()
    type()

    add()
    sub()
    mul()
    div()
    
def declaration():
    def __go__(self):
        return "var " + self.tokens[1].__go__()
    Declaration.__go__ = __go__

def affectation():
    def __go__(self):
        return self.tokens[0].__go__() + " = " + self.tokens[1].__go__()
    Affectation.__go__ = __go__

def declaffectation():
    def __go__(self):
        return self.tokens[1].__go__() + " := " + self.tokens[2].__go__()
    Declaffectation.__go__ = __go__

def functioncall():
    def __go__(self):
        return self.tokens[0].__go__() + self.tokens[1].__go__()
    FunctionCall.__go__ = __go__

def functiondef():
    def __go__(self):
        return self.tokens[0].__go__() + self.tokens[1].__go__() + self.tokens[2].__go__()
    FunctionDef.__go__ = __go__

def arguments():
    def __go__(self):
        string = "("
        for i in range(0, len(self.argument_list)-1):
            string = string + self.argument_list[i].__go__() + ", "
        string = string + self.argument_list[len(self.argument_list)-1].__go__() + ")"
        return string
    Arguments.__go__ = __go__

def parameters():
    def __go__(self):
        _size = len(self.types)

        if (_size == 0):
            return "()"

        string = "("
        for i in range(0, _size-1):
            string = string + self.types[i].__go__() + " " + self.names[i].__go__() + ", "
        string = string + self.types[_size-1].__go__() + " " + self.names[_size-1].__go__()
        string = string + ")"

        return string
    Parameters.__go__ = __go__

def block():
    def __go__(self):
        _size = len(self.instr_list)

        if (_size == 0):
            return " {}"
       
        string = " {\n"
        for i in range(0, _size):
            string = string + "\t" + self.instr_list[i].__go__() + "\n"
        string = string + "}\n"
        return string
    Block.__go__ = __go__

def name():
    def __go__(self):
        return self.__str__()
    Name.__go__ = __go__

def value():
    def __go__(self):
        return self.__str__()
    Value.__go__ = __go__

def type():
    def __go__(self):
        return self.__str__()
    Type.__go__ = __go__

def add():
    def __go__(self):
        return self.expr1.__go__() + " + " + self.expr2.__go__()
    Add.__go__ = __go__

def sub():
    def __go__(self):
        return self.expr1.__go__() + " - " + self.expr2.__go__()
    Sub.__go__ = __go__

def mul():
    def __go__(self):
        return self.expr1.__go__() + " * " + self.expr2.__go__()
    Mul.__go__ = __go__

def div():
    def __go__(self):
        return self.expr1.__go__() + " / " + self.expr2.__go__()
    Div.__go__ = __go__