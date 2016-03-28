# -*- coding: utf-8 -*-

from Exceptions import *

from Nodes.Node import *
from Nodes.Block import *
from Nodes.Expression import *

class Declaration(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        type = Type(data)
        name = Name(data, False)
        
        Instruction.__init__(self, [type, name]) # int v    
        
        data.Block.add(name.__str__(), type)

class Declaffectation(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        type = Type(data)
        name = Name(data, False)
        expr = Expression(data)
        Instruction.__init__(self, [type, name, expr]) # int v = 2 + 4
        
        data.Block.add(name.__str__(), type)
        # TODO test compability

class Affectation(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)
        name = Name(data, False)

        expr = Expression(data)
        Instruction.__init__(self, [name, expr]) # v = 2 + 4

        if (self.data.Block.get(name.__str__()) == None):
            self.data.Logger.logError("Error: " + name.__str__() + " is not known")
            raise ErrorEnvironment()

        data.Block.modify(name.__str__(), expr)
        # TODO test compability