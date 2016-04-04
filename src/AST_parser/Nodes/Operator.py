# -*- coding: utf-8 -*-

from Nodes.Node import *
from Nodes.Expression import *

# Abstract class of an operator
# An operator has a left expression and a right expression
class Operator(Expression):
    def __init__(self, data):
        Node.__init__(self, data)
        self.expr1 = None
        self.expr2 = None

    def setLeftExpr(self, expr):
        self.expr1 = expr
    def setRightExpr(self, expr):
        self.expr2 = expr

    # Resolve the final type of (expr1 OPERATOR expr2)
    def resolveType(self):
        # TODO
        pass

    def getType(self):
       return self.expr1.getType()

class Add(Operator): # Addition
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " + " + self.expr2.__str__()
class Sub(Operator): # Substraction
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " - " + self.expr2.__str__()
class Mul(Operator): # Multiplication
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " * " + self.expr2.__str__()
class Div(Operator): # Division
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " / " + self.expr2.__str()

class Access(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " . " + self.expr2.__str__()

    def getType(self):
       return self.expr2.getType()

class Equal(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " == " + self.expr2.__str__()

class NEqual(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " != " + self.expr2.__str__()

