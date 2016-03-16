# -*- coding: utf-8 -*-

import builtins

from Exceptions import ErrorParsing
from Logger import Logger

from Handler import Handler

# Everything is a node
class Node:
    def __init__(self):
        self.node_name = "_none_"

    def isTerminal(self): # pure virtual
        raise NotImplementedError("isTerminal interface method, problem...")

    # Search for content
    def fill(self): # pure virtual
        raise NotImplementedError("fill interface method, problem...")

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
    def create(string):
        return instr_dict[string]()

    def __init__(self, token_list):
        self.node_name = revDict(instr_dict, self.__class__) # get the right name in instruction dictinary
        self.tokens = token_list # list of tokens expected for instruction
        self.tokens_index = 0 # token list index
    
    def fill(self):
        while (not self.isComplete()): # fill instruction
            self.checkToken() # _/ ! \_ AST could become smaller
            self.tokens[self.tokens_index].fill()

            self.tokens_index += 1

    # Check if the token corresponds to the expected tokens
    def checkToken(self):
        token = Handler._s.next_string()
        if (not (token == self.tokens[self.tokens_index].getName())):
            Logger._s.logError("Error, unable to match token "+  token + " in discoverToken, waiting for " + self.tokens[self.tokens_index].getName())
            raise ErrorParsing()

    def isComplete(self):
        return (self.tokens_index >= len(self.tokens))

    def __str__(self):
        return self.getName() + ": " + self.tokens.__str__()

class Declaration(Instruction):
    def __init__(self):
        Instruction.__init__(self,  [Type(), Name(True), Expression()]) # int v = 2 + 4

class Affectation(Instruction):
    def __init__(self):
        Instruction.__init__(self,  [Name(), Value()]) # v = 2 + 4

# UNDEFINED _______________________________
class Arguments(Instruction):
    pass # TODO

# TERMINAL ________________________________
class Expression(Terminal):
    def __init__(self):
        self.node_name = revDict(expr_dict, self.__class__)

    def fill(self):
        expr = findExpr()
        self.__class__ = expr.__class__ # change __class__: Expression(4 + 4) -> Value(8)
        self.__dict__.update(expr.__dict__) # copy attributes

class Type(Expression):
    def __init__(self, keyword = None):
        Expression.__init__(self)
        if (keyword == None):
            self.keyword = "_none_" # int, float, ...
        else:
            self.keyword = keyword

    def fill(self):
        token = Handler._s.next_string()
        if (isTypeKeyword(token)): # check keyword
            self.keyword = token
        else:
            Logger._s.logError("Error: " + token + " is not a known type")
            raise ErrorParsing()

    def __str__(self):
        return self.keyword
    def __repr__(self):
        return self.__str__()

class Name(Expression):
    def __init__(self, b_decl = False):
        Expression.__init__(self)
        self.name = "_none_" # my_var1, ...
        self.decl = b_decl; # declaration or not

    def fill(self):
        token = Handler._s.next_string()
        if (not self.decl): # check environment
            if (not checkEnv(token)):
                Logger._s.logError("Error: " + token + " is not known")
                raise ErrorParsing()
        self.name = token

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

class Value(Expression):
    def __init__(self):
        Expression.__init__(self)
        self.val = "_none_" # 8, ...
        self.type = "_none_" # Type(int), ...

    def fill(self):
        token = Handler._s.next_string()
        self.type = findType(token) # find type
        self.val = token

    def __str__(self):
        return self.type + " " + self.val
    def __repr__(self):
        return self.__str__()

# LISTS ___________________________________
builtins.instr_dict = {"DECL": Declaration, "AFFECT": Affectation} # TODO complete
builtins.type_list = ["int", "float"] # TODO complete
builtins.expr_dict = {"EXPR" : Expression, "TYPE": Type, "NAME": Name, "VAL" : Value} # TODO complete

def revDict(dict, value):
    for k, v in dict.items():
        if v == value:
            return k

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
        return Type("float")
    return Type("int")

# Return the true expression object (such as Name, Value, Type, ...)
def findExpr():
    expr = None # expression

    if (Handler._s.check("[")): # list
        expression_list = []
        operator_list = []

        b_operator = False
        while not Handler._s.check("]"):
            string = Handler._s.next_string()

            if (not b_operator):
                expr = expr_dict[string]()
                expression_list.append(expr)
                expr.fill()
            else:
                operator_list.append(string)
            b_operator = not b_operator

        expr = factoriseExpr(expression_list, operator_list)
    else: # single expression
        expr = expr_dict[string]()
        expression_list.append(expr)
        expr.fill()
    
    return expr

def factoriseExpr(expression_list, operator_list):
   return None


    
