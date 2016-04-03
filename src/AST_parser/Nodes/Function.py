# -*- coding: utf-8 -*-

from Plus import *

from Exceptions import *
from Nodes.Node import *
from Nodes.Expression import *
from Nodes.Block import *
from Nodes.Instruction import *

# [Name] [Parameters] [Block]: function(int b) {...}
class FunctionDef(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.type = Type(data)
        self.name = Name(data, False)
        self.parm = Parameters(data)
        self.block = Block(data.Block, data)

        self.type.fill()
        self.name.fill()

        data.Block = self.block # parm need to be in block environment
        self.parm.fill()
        data.Block = self.block.parent
        
        data.Block.addFunction(self.name.__str__(), self.parm.__key__(), self.type) # add function to environment
        self.block.fill()

    def __str__(self):
        return self.type.__str__() + " " + self.name.__str__() + self.parm.__str__() + self.block.__str__()

# [Name] [Arguments]: function(4+5, c)
class FunctionCall(Expression): # this node is kind of special since it's both an Instruction and an Expression
    def __init__(self, data):
        Expression.__init__(self, data)
        self._type = None

        self.name = Name(data, False)
        self.args = Arguments(data)

        self.name.fill()
        self.args.fill()

        _class = data.Block.getClass(data._class.__str__())
        if (_class != None):
            self._type = _class.getFunction(self.name.__str__(), self.args.__key__())
            if (self._type == None):
                data.Logger.logError("Error: " + self.name.__str__() + self.args.__key__() +  " function is not known in class " + data._class.__str__())
                raise ErrorEnvironment()
        else: # test if function exist in environment (name + args)
            self._type = data.Block.getFunction(self.name.__str__(), self.args.__key__())
            if (self._type == None):
                data.Logger.logError("Error: " + self.name.__str__() + self.args.__key__() +  " function is not known")
                raise ErrorEnvironment()
        self.filled = True
            
    def getType(self): # returns type of function
        return self._type

    def __str__(self):
        return self.name.__str__()  + self.args.__str__()

# {[Expr]}*: (4+2, b)
class Arguments(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.argument_list = [] # list of expressions

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                self.data.Handler.checkString(self.node_name) # check for the right statement
            if (self.data.Handler.check("[")):
                while (not self.data.Handler.check("]")):
                    expr = Expression(self.data)
                    expr.fill()
                    self.argument_list.append(expr)
            self.filled = True

    def __str__(self):
        _size = len(self.argument_list)
        if (_size == 0):
            return "()"

        string = "("
        for i in range(0, _size-1):
            string = string + self.argument_list[i].__str__() + ", "
        string = string + self.argument_list[_size-1].__str__() + ")"

        return string

    def __key__(self): # return an hashmap representation of arguments of the function (list of type)
        types = []
        for a in self.argument_list:
            types.append(a.getType())

        return types.__repr__()

# {[Type] [Name]}*: (int a, float b)
class Parameters(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.types = [] # type list
        self.names = [] # name list

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                    self.data.Handler.checkString(self.node_name) # check for the right statement
            if (self.data.Handler.check("[")):
                while (not self.data.Handler.check("]")):
                    type = Type(self.data)
                    type.fill()
                    self.types.append(type)

                    name = Name(self.data, False)
                    name.fill()
                    self.names.append(name)

                    self.data.Block.add(name.__str__(), type) # add parameters to environment
            self.filled = True

    def __str__(self):
        _size = len(self.types)
        if (_size == 0):
            return "()"

        string = "("
        for i in range(0, _size-1):
            string = string + self.types[i].__str__() + " " + self.names[i].__str__() + ", "
        string = string + self.types[_size-1].__str__() + " " + self.names[_size-1].__str__()
        string = string + ")"

        return string

    def __key__(self): # return an hashmap representation of parameters of the function (list of type)
        return self.types.__repr__()

