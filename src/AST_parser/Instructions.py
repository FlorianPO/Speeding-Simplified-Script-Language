# -*- coding: utf-8 -*-

import builtins

from Exceptions import ErrorParsing
from Exceptions import Logger

# NODE ____________________________________
class Node:
    def __init__(self):
        self.node_name = "_none_"

    def isTerminal(self): # pure virtual
        raise NotImplementedError("isTerminal interface method, problem...")

    def feedMe(self, token): # pure virtual
        raise NotImplementedError("feedMe interface method, problem...")

    def getName(self):
        return self.node_name

class Terminal(Node):
    def isTerminal(self):
        return True

class nonTerminal(Node):
    def isTerminal(self):
        return False

# NON TERMINAL ____________________________
class Instruction(nonTerminal):
    def __init__(self, token_list):
        self.tokens = token_list
        self.tokens_index = 0
        
    def discoverToken(self, token):
        if (not (token == self.tokens[self.tokens_index].getName())):
            Logger._s.log("Error, unable to match token "+  token + " in discoverToken", 1)
            raise ErrorParsing()

    def feedToken(self, token):
        self.tokens[self.tokens_index].feedMe(token)
        self.tokens_index += 1

    def isComplete(self):
        return (self.tokens_index >= len(self.tokens))

    def __str__(self):
        return self.getName() + ": " + self.tokens.__str__()

class Declaration(Instruction):
    def __init__(self):
        self.node_name = "DECL"
        Instruction.__init__(self,  [Type(), Name(), Value()]) # int a = 4

# UNDEFINED _______________________________
class Arguments(Instruction):
    pass # TODO

# TERMINAL ________________________________
class Expression(Terminal):
    def __init__(self):
        self.node_name = "EXPR"

    def feedMe(self, token):
        self.__class__ = findExpr(token) # WARNING: this may not work

class Type(Expression):
    def __init__(self):
        self.keyword = "_none_"
        self.node_name = "TYPE"

    def feedMe(self, token):
        if (isTypeKeyword(token)): # check keyword
            self.keyword = token
        else:
            Logger._s.log("Error: " + token + " is not a known type", 1)
            raise ErrorParsing()

    def __str__(self):
        return self.keyword
    def __repr__(self):
        return self.__str__()

class Name(Expression):
    def __init__(self, b_decl = False):
        self.name = "_none_"
        self.decl = b_decl; # declaration or not
        self.node_name = "NAME"

    def feedMe(self, token):
        if (not self.decl): # check environment
            if (not checkEnv(token)):
                Logger._s.log("Error: " + token + " is not a known", 1)
                raise ErrorParsing()
        self.name = token

    def __str__(self):
        if (self.decl):
            return self.name + " (DECL)"
        return self.name
    def __repr__(self):
        return self.__str__()

class Value(Expression):
    def __init__(self):
        self.val = "_none_"
        self.type = "_none_"
        self.node_name = "VAL"

    def feedMe(self, token):
        self.type = findType(token) # find type
        self.val = token

    def __str__(self):
        return self.type + " " + self.val
    def __repr__(self):
        return self.__str__()

# LISTS ___________________________________
builtins.instr_dict = {"DECL": Declaration} # TODO complete
builtins.type_list = ["int", "float"] # TODO complete
builtins.expr_dict = {"TYPE": Type.__class__, "NAME": Name.__class__, "VALUE" : Value.__class__} # TODO complete

# FUNCTIONS _______________________________
# Check if the given string match a type keyword such as "int"
def isTypeKeyword(string):
    return (string in type_list)

# Check if a name var exists in the environment (return true if valid)
def checkEnv(string):
    # TODO
    return True

# Find the best matching type of a given value, ex: 1.5 -> float
def findType(string):
    if (string.find('.') >= 0):
        return "float"
    return "int"

# Return the true expression object (such as Name, Value, Type, ...)
def findExpr(string):
    class_name = expr_dict.get(string)
   
    # TODO recursive calls -> where all is performed
    return class_name
