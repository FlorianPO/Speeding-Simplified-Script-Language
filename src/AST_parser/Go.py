# -*- coding: utf-8 -*-

from Nodes.Instruction import *
from Nodes.Expression import *
from Nodes.Function import *
from Nodes.Object import *
from Nodes.Condition import *
from Nodes.Operator import *
from Nodes.Block import *
from Nodes.FunctionSystem import *

_INDENT_ = None
def init():
    global _INDENT_
    _INDENT_ = ""

    DECLARATION()
    DECLAFFECTATION()
    AFFECTATION()
    DECLARATIONINCLASS()
    
    FUNCTIONDEF()
    METHODEDEF()
    DMAIN()
    CONSTRUCTORDEF()
    FUNCTIONCALL()
    ECHO()
    ECHOLN()
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
    INF()
    SUP()
    INFEGAL()
    SUPEGAL()

    NAME()
    VALUE()
    TYPE()

    ADD()
    SUB()
    MUL()
    DIV()
    PARENTHESE()
    
def DECLARATION():
    def __go__(self):
        return "var " + self.name.__go__() + " " + self.type.__go__()
    Declaration.__go__ = __go__
    
def DECLARATIONINCLASS():
    def __go__(self):
        return self.name.__go__() + " " + self.type.__go__()
    DeclarationInClass.__go__ = __go__

def AFFECTATION():
    def __go__(self):
        return self.name.__go__() + " = " + self.expr.__go__()
    Affectation.__go__ = __go__

def DECLAFFECTATION():
    def __go__(self):
        return "var " + self.name.__go__() + " " + self.type.__go__() + " = " + self.expr.__go__()
    Declaffectation.__go__ = __go__

def FUNCTIONCALL():
    def __go__(self):
        return self.name.__go__() + self.args.__go__()
    FunctionCall.__go__ = __go__

def ECHO():
    def __go__(self):
        return "fmt.Print(" + self.expr.__go__() + ")"
    Echo.__go__ = __go__

def ECHOLN():
    def __go__(self):
        return "fmt.Println(" + self.expr.__go__() + ")"
    Echoln.__go__ = __go__

def FUNCTIONDEF():
    def __go__(self):
        string = "func " + self.name.__go__() + self.parm.__go__()
        if(self.type.__str__() != "void"):
            string = string + " " + self.type.__go__()
        return string  + " " + self.block.__go__()
    FunctionDef.__go__ = __go__
    
def METHODEDEF():
    def __go__(self):
        string = "func (this " + self.class_name + ") " + self.name.__go__() + self.parm.__go__()
        if (self.type.__str__() != "void"):
            string = string + " " + self.type.__go__()
        return string + " " + self.block.__go__()
    MethodDef.__go__ = __go__

def DMAIN():
    def __go__(self):
        return "func " + "main" + self.parm.__go__()  + self.block.__go__()
    DMain.__go__ = __go__


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
            string = string + self.names[i].__go__() + " " + self.types[i].__go__() + ", "
        string = string + self.names[_size-1].__go__() + " " + self.types[_size-1].__go__()
        string = string + ")"

        return string
    Parameters.__go__ = __go__

def BLOCK():
    def __go__(self, accolade=True):
        _size = len(self.instr_list)

        if (_size == 0 and accolade):
            return " {}"
        elif (_size == 0):
            return ""
       
        if (accolade):
           global _INDENT_
           _PREVIOUS_INDENT_ = _INDENT_
           _INDENT_ = _INDENT_ + "\t"
           string = _PREVIOUS_INDENT_ + "{\n"
           for i in range(0, _size):
               string = string + _INDENT_ + self.instr_list[i].__go__() + "\n"
           string = string + _PREVIOUS_INDENT_ + "}"
           _INDENT_ = _PREVIOUS_INDENT_
        else:
           for i in range(0, _size):
               string = self.instr_list[i].__go__() + "\n"
               
        return string
    Block.__go__ = __go__

def CLASSDEF():
    def __go__(self):
        meth_list = []

        i = 0
        while i < len(self.block.instr_list):
            if isinstance(self.block.instr_list[i], MethodDef):
                print(i)
                meth_list.append(self.block.instr_list[i])
                del self.block.instr_list[i]
                i = i-1
            i = i+1
        
        string = ""
        for i in range(0, len(meth_list)):
            string = string + meth_list[i].__go__() + "\n"
            
        return "type " + self.name.__go__() + " struct" + self.block.__go__() + "\n" + string
    ClassDef.__go__ = __go__

def ACCESS():
    def __go__(self):
        return self.expr1.__go__() + "." + self.expr2.__go__()
    Access.__go__ = __go__

def RETURN():
    def __go__(self):
        if (self.expr == None):
            return ""
        else:
            return "return " + self.expr.__go__()
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
 
def INF():
    def __go__(self):
        return self.expr1.__go__() + " < " + self.expr2.__go__()
    Inf.__go__ = __go__

def SUP():
    def __go__(self):
        return self.expr1.__go__() + " > " + self.expr2.__go__()
    Sup.__go__ = __go__

def INFEGAL():
    def __go__(self):
        return self.expr1.__go__() + " <= " + self.expr2.__go__()
    InfEgal.__go__ = __go__

def SUPEGAL():
    def __go__(self):
        return self.expr1.__go__() + " >= " + self.expr2.__go__()
    SupEgal.__go__ = __go__

def IF():
    def __go__(self):
        return "if " + self.expr.__go__() + self.block.__go__()
    If.__go__ = __go__

def ELSE():
    def __go__(self):
        return "else" + self.block.__go__()
    Else.__go__ = __go__

def ELIF():
    def __go__(self):
        return "else if " + self.expr.__go__() + self.block.__go__()
    Elif.__go__ = __go__

def WHILE():
    def __go__(self):
        return "for " + self.expr.__go__()  + self.block.__go__()
    While.__go__ = __go__

def DOWHILE():
    def __go__(self):
        return self.block.__go__(False) + _INDENT_ +"for " + self.expr.__go__() + self.block.__go__()
    DoWhile.__go__ = __go__

def NAME():
    def __go__(self):
        return self.__str__()
    Name.__go__ = __go__

def VALUE():
    def __go__(self):
        if(self.getType().__str__() == "string"):
            return '"'+self.__str__()[1:-1]+'"'
        else :
            return self.__str__()
    Value.__go__ = __go__

def TYPE():
    def __go__(self):
        if (self.__str__() == "float"):
            return self.__str__() + "32"
        else:
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

def PARENTHESE():
    def __go__(self):
        return "(" + self.expr.__go__() + ")"
    Parenthese.__go__ = __go__

