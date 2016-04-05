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
        self.compability = []

    def setExpr(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        
        if (self.data.check_type_compability):
            if (self.compability != []):
                if (not (self.expr1.getType().__str__() in self.compability and self.expr2.getType().__str__() in self.compability)):
                    data.Logger.logError("Error: " + self.expr1.getType().__str__() + " and " + self.expr2.getType().__str__() + " are not compatible")
                    raise ErrorType()
            else:
                if (self.expr1.getType().__str__() != self.expr2.getType().__str__()):
                    data.Logger.logError("Error: " + self.expr1.getType().__str__() + " and " + self.expr2.getType().__str__() + " are not compatible")
                    raise ErrorType()

    def getType(self):
       return self.expr1.getType()

class Add(Operator): # Addition
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " + " + self.expr2.__str__()
class Sub(Operator): # Substraction
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " - " + self.expr2.__str__()
class Mul(Operator): # Multiplication
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " * " + self.expr2.__str__()
class Div(Operator): # Division
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " / " + self.expr2.__str()

class Access(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + "." + self.expr2.__str__()

    def setExpr(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def getType(self):
       return self.expr2.getType()

class Equal(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " == " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class NEqual(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
    def __str__(self):
        return self.expr1.__str__() + " != " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class Inf(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " < " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class Sup(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " > " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class InfEgal(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " <= " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class SupEgal(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["int", "float"]
    def __str__(self):
        return self.expr1.__str__() + " >= " + self.expr2.__str__()

    def getType(self):
       return Type(self.data, "bool")

class Or(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["bool"]
    def __str__(self):
        return self.expr1.__str__() + " or " + self.expr2.__str__()

class And(Operator):
    def __init__(self, data):
        Operator.__init__(self, data)
        self.compability = ["bool"]
    def __str__(self):
        return self.expr1.__str__() + " and " + self.expr2.__str__()

class Parenthese(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data)
        self.expr.fill(False)

    def __str__(self):
        return "( " + self.expr.__str__() + " )"

