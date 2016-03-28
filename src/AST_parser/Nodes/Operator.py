from Nodes.Node import *
from Nodes.Expression import *

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

    def getType(self):
       return Type(self.data, "int")

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