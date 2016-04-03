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
        # TODO test if boolean

# [Expr] [Block]: while (a == 1) {...}
class While(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data) # must be a boolean
        self.block = Block(data.Block, data)
       
        self.expr.fill()
        self.block.fill()
        # TODO test if boolean

# [Block]: else {...}
class Else(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.block = Block(data.Block, data)
        self.block.fill()
        # TODO "else" if "if" before 

# [Expr] [Block]: elif (True) {...}
class Elif(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = Expression(data) # must be a boolean
        self.block = Block(data.Block, data)
       
        self.expr.fill()
        self.block.fill()
        # TODO test if boolean

# [Block] [Expr]: do {...} while (b == 2) 
class DoWhile(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.block = Block(data.Block, data)
        self.expr = Expression(data) # must be a boolean
       
        self.block.fill()
        self.expr.fill()
        # TODO test if boolean
