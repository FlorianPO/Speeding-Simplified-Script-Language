# -*- coding: utf-8 -*-

from Plus import *

from Exceptions import *
from Nodes.Node import *
from Nodes.Expression import *
from Nodes.Block import *
from Nodes.Instruction import *

# [Name] [Parameters] [Block]: function(int b) {...}
class FunctionDef(Instruction):
    def __init__(self, data):
        Node.__init__(self, data)

        type = Type(data)
        name = Name(data, False)
        parm = Parameters(data)
        block = Block(data.Block, data)
        
        data.Block = block # parm need to be in block environment
        Instruction.__init__(self, [type, name, parm, block])
        data.Block = block.parent # retrieve old block
        
        data.Block.addFunction(name.__str__(), parm.__key__(), type) # add function to environment

# [Name] [Arguments]: function(4+5, c)
class FunctionCall(Instruction, Expression): # this node is kind of special since it's both an Instruction and an Expression
    def __init__(self, data):
        Expression.__init__(self, data)

        name = Name(data, False)
        args = Arguments(self.data)
        
        Instruction.__init__(self, [name, args])
        
        if (self.data.Block.getFunction(name.__str__(), args.__key__()) == None): # test if function exist in environment (name + args)
            self.data.Logger.logError("Error: " + name.__str__() + args.__key__() +  " function is not known")
            raise ErrorEnvironment()

    def getType(self): # returns type of function
        return self.data.Block.getFunction(self.tokens[0].__str__(), self.tokens[1].__key__())

# {[Expr]}*: (4+2, b)
class Arguments(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.argument_list = [] # list of expressions

    def fill(self):
        if (self.data.Handler.check("[")):
            while (not self.data.Handler.check("]")):
                Instruction.checkString(self.data, revDict(self.data.all_dict, Expression)) # check for Expression statement
                expr = Expression(self.data)
                expr.fill()
                self.argument_list.append(expr)

    def __str__(self):
        string = "("
        for i in range(0, len(self.argument_list)-1):
            string = string + self.argument_list[i].__str__() + ", "
        string = string + self.argument_list[len(self.argument_list)-1].__str__() + ")"
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

    def fill(self):
        if (self.data.Handler.check("[")):
            while (not self.data.Handler.check("]")):
                Instruction.checkString(self.data, revDict(self.data.all_dict, Type)) # check for Type statement
                type = Type(self.data)
                type.fill()
                self.types.append(type)

                Instruction.checkString(self.data, revDict(self.data.all_dict, Name)) # check for Name statement
                name = Name(self.data, False)
                name.fill()
                self.names.append(name)

                self.data.Block.add(name.__str__(), Expression(self.data)) # add parameters to environment

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
