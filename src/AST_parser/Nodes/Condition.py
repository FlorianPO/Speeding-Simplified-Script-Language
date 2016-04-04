# -*- coding: utf-8 -*-

from Nodes.Node import *
from Nodes.Expression import *
from Nodes.Block import *

# [Expr] [Block]: if (a == 1) {...}
class If(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data) # must be a boolean
        self.block = Block(data.Block, data)
       
        self.expr.fill()
        self.block.fill()
        
        if (self.expr.getType().__str__() != "bool"): # test type compability
            data.Logger.logError("Error: bool and " + self.expr.getType().__str__() + " are not compatible")
            raise ErrorType()

    def __str__(self):
        return "if (" + self.expr.__str__() + ")" + self.block.__str__()

# [Expr] [Block]: while (a == 1) {...}
class While(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data) # must be a boolean
        self.block = Block(data.Block, data)
       
        self.expr.fill()
        self.block.fill()
        
        if (self.expr.getType().__str__() != "bool"): # test type compability
            data.Logger.logError("Error: bool and " + self.expr.getType().__str__() + " are not compatible")
            raise ErrorType()

    def __str__(self):
        return "while (" + self.expr.__str__() + ")" + self.block.__str__()

# [Block]: else {...}
class Else(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.block = Block(data.Block, data)
        self.block.fill()

    def __str__(self):
        return "else" + self.block.__str__()

# [Expr] [Block]: elif (True) {...}
class Elif(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data) # must be a boolean
        self.block = Block(data.Block, data)
       
        self.expr.fill()
        self.block.fill()
        
        if (self.expr.getType().__str__() != "bool"): # test type compability
            data.Logger.logError("Error: bool and " + self.expr.getType().__str__() + " are not compatible")
            raise ErrorType()

    def __str__(self):
        return "else if (" + self.expr.__str__() + ")" + self.block.__str__()

# [Block] [Expr]: do {...} while (b == 2) 
class DoWhile(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.block = Block(data.Block, data)
        self.expr = Expression(data) # must be a boolean
       
        self.block.fill()
        self.expr.fill()
       
        if (self.expr.getType().__str__() != "bool"): # test type compability
            data.Logger.logError("Error: bool and " + self.expr.getType().__str__() + " are not compatible")
            raise ErrorType()

    def __str__(self):
        return "do" + self.block.__str__() + " while (" + self.expr.__str__() + ")"