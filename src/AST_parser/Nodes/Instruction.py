# -*- coding: utf-8 -*-

from Exceptions import *

from Nodes.Node import *
from Nodes.Block import *
from Nodes.Expression import *

# [Type] [Name]: int variable
class Declaration(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)

        type = Type(data)
        name = Name(data, False)
        Instruction.__init__(self, [type, name])
        
        data.Block.add(name.__str__(), type) # add variable to environment

# [Type] [Name] [Expr]: int variable = 8
class Declaffectation(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)

        type = Type(data)
        name = Name(data, False)
        expr = Expression(data)
        Instruction.__init__(self, [type, name, expr]) # int v = 2 + 4
        
        data.Block.add(name.__str__(), type) # add variable to environment
        # TODO test compability of type and expr

# [Name] [Expr]: variable = 7
class Affectation(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)

        name = Name(data, False)
        expr = Expression(data)
        Instruction.__init__(self, [name, expr])

        if (self.data.Block.get(name.__str__()) == None): # test if variable exists in environment
            self.data.Logger.logError("Error: " + name.__str__() + " is not known")
            raise ErrorEnvironment()

        data.Block.modify(name.__str__(), expr) # modify variable in environment
        # TODO test compability of variable type and expr