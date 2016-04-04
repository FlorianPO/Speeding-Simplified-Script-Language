# -*- coding: utf-8 -*-

from Nodes.Instruction import *
from Nodes.Expression import *
from Nodes.Function import *
from Nodes.Object import *
from Nodes.Condition import *
from Nodes.Operator import *
from Nodes.Block import *

_INDENT_ = None
def init():
    global _INDENT_
    _INDENT_ = ""

    DECLARATION()
    DECLAFFECTATION()
    AFFECTATION()
    
    FUNCTIONDEF()
    CONSTRUCTORDEF()
    FUNCTIONCALL()
    ARGUMENTS()
    PARAMETERS()
    BLOCK()

    CLASSDEF()
    ACCESS()

    RETURN()
    BREAK()

    IF()
    ELSE()
    ELIF()
    WHILE()
    DOWHILE()
    EQUAL()
    NEQUAL()

    NAME()
    VALUE()
    TYPE()

    ADD()
    SUB()
    MUL()
    DIV()
    
def DECLARATION():
    def __go__(self):
        return "var " + self.name.__go__()
    Declaration.__go__ = __go__

def AFFECTATION():
    def __go__(self):
        return self.name.__go__() + " = " + self.expr.__go__()
    Affectation.__go__ = __go__

def DECLAFFECTATION():
    def __go__(self):
        return self.name.__go__() + " := " + self.expr.__go__()
    Declaffectation.__go__ = __go__

def FUNCTIONCALL():
    def __go__(self):
        return self.name.__go__() + self.args.__go__()
    FunctionCall.__go__ = __go__

def FUNCTIONDEF():
    def __go__(self):
        return self.type.__go__() + " " + self.name.__go__() + self.parm.__go__() + self.block.__go__() + "\n"
    FunctionDef.__go__ = __go__

def CONSTRUCTORDEF():
    def __go__(self):
        return self.name.__go__() + self.parm.__go__() + self.block.__go__() + "\n"
    ConstructorDef.__go__ = __go__

def ARGUMENTS():
    def __go__(self):
        _size = len(self.argument_list)

        if (_size == 0):
            return "()"

        string = "("
        for i in range(0, _size-1):
            string = string + self.argument_list[i].__go__() + ", "
        string = string + self.argument_list[_size-1].__go__() + ")"
        return string
    Arguments.__go__ = __go__

def PARAMETERS():
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

def BLOCK():
    def __go__(self):
        _size = len(self.instr_list)

        if (_size == 0):
            return " {}"
       
        global _INDENT_
        _PREVIOUS_INDENT_ = _INDENT_
        _INDENT_ = _INDENT_ + "\t"

        string = " {\n"
        for i in range(0, _size):
            string = string + _INDENT_ + self.instr_list[i].__go__() + "\n"
        string = string + _PREVIOUS_INDENT_ + "}"
        
        _INDENT_ = _PREVIOUS_INDENT_

        return string
    Block.__go__ = __go__

def CLASSDEF():
    def __go__(self):
        return "class " + self.name.__go__() + self.block.__go__()
    ClassDef.__go__ = __go__

def ACCESS():
    def __go__(self):
        return self.expr1.__go__() + "." + self.expr2.__go__()
    Access.__go__ = __go__

def RETURN():
    def __go__(self):
        if (self.expr == None):
            return "return;"
        else:
            return "return " + self.expr.__go__() + ";"
    Return.__go__ = __go__

def BREAK():
    def __go__(self):
        return "break"
    Break.__go__ = __go__

def EQUAL():
    def __go__(self):
        return self.expr1.__go__() + " == " + self.expr2.__go__()
    Equal.__go__ = __go__

def NEQUAL():
    def __go__(self):
        return self.expr1.__go__() + " != " + self.expr2.__go__()
    NEqual.__go__ = __go__

def IF():
    def __go__(self):
        return "if (" + self.expr.__go__() + ")" + self.block.__go__()
    If.__go__ = __go__

def ELSE():
    def __go__(self):
        return "else" + self.block.__go__()
    Else.__go__ = __go__

def ELIF():
    def __go__(self):
        return "else if (" + self.expr.__go__() + ")" + self.block.__go__()
    Elif.__go__ = __go__

def WHILE():
    def __go__(self):
        return "while (" + self.expr.__go__() + ")" + self.block.__go__()
    While.__go__ = __go__

def DOWHILE():
    def __go__(self):
        return "do" + self.block.__go__() + " while (" + self.expr.__go__() + ")"
    DoWhile.__go__ = __go__

def NAME():
    def __go__(self):
        return self.__str__()
    Name.__go__ = __go__

def VALUE():
    def __go__(self):
        return self.__str__()
    Value.__go__ = __go__

def TYPE():
    def __go__(self):
        return self.__str__()
    Type.__go__ = __go__

def ADD():
    def __go__(self):
        return self.expr1.__go__() + " + " + self.expr2.__go__()
    Add.__go__ = __go__

def SUB():
    def __go__(self):
        return self.expr1.__go__() + " - " + self.expr2.__go__()
    Sub.__go__ = __go__

def MUL():
    def __go__(self):
        return self.expr1.__go__() + " * " + self.expr2.__go__()
    Mul.__go__ = __go__

def DIV():
    def __go__(self):
        return self.expr1.__go__() + " / " + self.expr2.__go__()
    Div.__go__ = __go__
