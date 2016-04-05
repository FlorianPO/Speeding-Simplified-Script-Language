# -*- coding: utf-8 -*-

from Nodes.Function import *
from Nodes.Expression import *
from Nodes.Function import *
from Nodes.Block import *

# [Name] [Parameters] [Block]: function(int b) {...}
class ClassDef():
    def __init__(self, data):
        Node.__init__(self, data)

        self.name = Name(data, False)
        self.block = Block(data.Block, data)

        self.name.fill()
        data.Block.addClass(self.name.__str__(), self.block) # add class to environment (it may be used inside the class itself)
        data._class_name = self.name.__str__()
        self.block.fill()

    def __str__(self):
        return "class " + self.name.__str__() + self.block.__str__()

class ConstructorDef(FunctionDef):
    def __init__(self, data):
        Node.__init__(self, data)

        self.class_name = data._class_name
        self.name = Name(data, False)
        self.parm = Parameters(data)
        self.block = Block(data.Block, data)

        self.name.fill()
        data.Block = self.block # parm need to be in block environment
        self.parm.fill()
        data.Block = self.block.parent # retrieve old block
        
        data.Block.parent.addFunction(self.name.__str__(), self.parm.__key__(), Type(data, data._class_name)) # add constructor to environment of the class
        self.block.fill()
        
    def __str__(self):
        return self.name.__str__() + self.parm.__str__() + self.block.__str__()
        
class MethodDef(FunctionDef):
    def __init__(self, data):
        Node.__init__(self, data)

        self.class_name = data._class_name
        self.type = Type(data)
        self.name = Name(data, False)
        self.parm = Parameters(data)
        self.block = Block(data.Block, data)

        self.type.fill()
        self.name.fill()
        data.Block = self.block # parm need to be in block environment
        self.parm.fill()
        data.Block = self.block.parent # retrieve old block
        data.Block.add("this", Type(data, self.name.__str__())) # add this
        
        data.Block.parent.addFunction(self.name.__str__(), self.parm.__key__(), self.type) # add constructor to environment of the class
        self.block.fill()
        
    def __str__(self):
        return self.type.__str__() + self.name.__str__() + self.parm.__str__() + self.block.__str__()
        
class DeclarationInClass(Declaration):
    def __init__(self, data):
        Declaration.__init__(self, data)
        
