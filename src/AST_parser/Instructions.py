# -*- coding: utf-8 -*-

import builtins

from Exceptions import *

# Everything is a node
class Node:
    def __init__(self, data):
        self.node_name = revDict(data.all_dict, self.__class__) # get the right name
        self.data = data

    # Search for content
    def fill(self): # pure virtual
        raise NotImplementedError("fill interface method, problem...")

    def getName(self):
        return self.node_name
    def __repr__(self):
        return self.__str__()

# NON TERMINAL ____________________________
class Instruction(Node):
    def create(string, data):
        return data.instr_dict[string](data)

    def __init__(self, token_list):
        self.tokens = token_list # list of tokens expected for instruction
        self.tokens_index = 0 # token list index
        self.fill()

    def fill(self):
        while (not self.isComplete()): # fill instruction
            self.checkToken() # _/ ! \_ AST could become smaller
            self.tokens[self.tokens_index].fill()

            self.tokens_index += 1

    # Check if the token corresponds to the expected tokens
    def checkToken(self):
        token = self.data.Handler.next_string()
        if (not (token == self.tokens[self.tokens_index].getName())):
            self.data.Logger.logError("Error, unable to match token "+  token + " in discoverToken, waiting for " + self.tokens[self.tokens_index].getName())
            raise ErrorParsing()

    def isComplete(self):
        return (self.tokens_index >= len(self.tokens))

    def __str__(self):
        return self.node_name + ": " + self.tokens.__str__()

class Declaration(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        type = Type(data)
        name = Name(data, True)
        expr = Expression(data)
        Instruction.__init__(self, [type, name, expr]) # int v = 2 + 4
        
        name.setType(type)

        data.Block.add(name.__str__(), expr)

        # TODO test compability

class Affectation(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        name = Name(data)
        expr = Expression(data)
        Instruction.__init__(self, [name, expr]) # v = 2 + 4
        data.Block.modify(name.__str__(), expr)
        # TODO test compability

class FunctionDef(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        name = Name(data)
        args = Arguments(data)
        Instruction.__init__(self, [name, args]) # v = 2 + 4

# UNDEFINED _______________________________
class Arguments(Instruction):
    pass # TODO

class Type(Node):
    def __init__(self, data, keyword = None):
        Node.__init__(self, data)
        if (keyword == None):
            self.keyword = "_none_" # int, float, ...
        else:
            self.keyword = keyword

    def fill(self):
        token = self.data.Handler.next_string()
        if (token in self.data.type_list): # check keyword
            self.keyword = token
        else:
            self.data.Logger.logError("Error: " + token + " is not a known type")
            raise ErrorParsing()

    def __str__(self):
        return self.keyword

# Expression ________________________________
class Expression(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.type = None
        self.value_s = "_none_" # string, literal value

    def fill(self):
        expr = findExpr(self.data)
        self.__class__ = expr.__class__ # change __class__: Expression(4 + 4) -> Add(4, 4)
        self.__dict__.update(expr.__dict__) # copy attributes

    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type

class Name(Expression):
    def __init__(self, data, b_decl = False):
        Expression.__init__(self, data)
        self.decl = b_decl; # declaration or not

    def fill(self):  
        token = self.data.Handler.next_string()
        if (not self.decl): # not a declaration
            expr = self.data.Block.get(token)
            if (expr == None):
                self.data.Logger.logError("Error: " + token + " is not known")
                raise ErrorEnvironment()
            self.type = expr.getType()
        self.value_s = token

    def __str__(self):
        return self.value_s

class Value(Expression):
    def __init__(self, data):
        Expression.__init__(self, data)

    def fill(self):
        token = self.data.Handler.next_string()
        self.type = findType(self.data, token) # find type
        self.value_s = token

    def __str__(self):
        return self.value_s

class FunctionCall(Expression):
    def __init__(self, data):
        Expression.__init__(self, data)
        self.args = None

    def fill(self):
        token = self.data.Handler.next_string()
        self.value_s = token
        self.args = findArgs()

        block = self.data.Block.getFunction(self.value_s, self.args)
        if (block == None):
            self.data.Logger.logError("Error: " + self.__str__() + " function is not known")
            raise ErrorEnvironment()

    def __str__(self):
        return self.value_s + self.args.__str__()

# OPERATOR ________________________________
class Operator(Expression):
    def __init__(self, data):
        Node.__init__(self, data)
        self.expr1 = None
        self.expr2 = None

    def setLeftExpr(self, expr):
        self.expr1 = expr
    def setRightExpr(self, expr):
        self.expr2 = expr

    def resolveType(self):
        # TODO
        pass

class Add(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " + " + self.expr2.__str__()
class Sub(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " - " + self.expr2.__str__()
class Mul(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " * " + self.expr2.__str__()
class Div(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " / " + self.expr2.__str__()

# FUNCTIONS _______________________________
def revDict(dict, value):
    for k, v in dict.items():
        if v == value:
            return k

# Find the best matching type of a given value, ex: 1.5 -> float
def findType(data, string):
    if (string.find('.') >= 0):
        return Type(data, "float")
    return Type(data, "int")

def findValue(string, type):
    pass

# Return the true expression object (such as Name, Value, Type, ...)
def findExpr(data):
    if (data.Handler.check("[")): # list
        left_expr = None
        right_expr = None
        operator = None
        
        left_expr = findExpr(data)  
        string = data.Handler.next_string()
        oper = data.oper_dict[string](data)
        right_expr = findExpr(data)

        oper.setLeftExpr(left_expr)
        oper.setRightExpr(right_expr)
        
        if (not data.Handler.check("]")):
            self.data.Logger.logError("Error: unable to find end of expression")
            raise ErrorParsing()

        return oper
    else: # single expression
        string = data.Handler.next_string()
        expr = data.expr_dict[string](data)
        expr.fill()

        return expr

# ADD(4, ADD(4, 4))
def factoriseExpr(data, expression_list, operator_list):
    expr = None
    if (len(operator_list) > 0):
        expr = operator_list[0]
        expr.setLeftExpr(expression_list[0])
        del expression_list[0]
        del operator_list[0]
        expr.setRightExpr(factoriseExpr(data, expression_list, operator_list))
    else:
        expr = expression_list[0]

    return expr



    
