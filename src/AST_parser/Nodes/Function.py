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
        name = Name(data, False)
        block = Block(data.Block, data)
        parm = Parameters(data)
        
        data.Block = block
        Instruction.__init__(self, [name, parm, block])
        data.Block = block.parent
        
        data.Block.addFunction(name.__str__(), parm.__key__(), block)

# [Name] [Arguments]: function(4+5, c)
class FunctionCall(Instruction, Expression):
    def __init__(self, data):
        Expression.__init__(self, data)

        name = Name(data, False)
        args = Arguments(self.data)
        
        Instruction.__init__(self, [name, args])
        
        if (self.data.Block.getFunction(name.__str__(), args.__key__()) == None):
            self.data.Logger.logError("Error: " + name.__str__() + args.__key__() +  " function is not known")
            raise ErrorEnvironment()

    def getType(self): # TODO
        return Type(self.data, "int")

# {[Expr]}*: (4+2, b)
class Arguments(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.argument_list = []

    def fill(self):
        if (self.data.Handler.check("[")): # list
            while (not self.data.Handler.check("]")):
                Instruction.checkString(self.data, revDict(self.data.all_dict, Expression))
                expr = Expression(self.data)
                expr.fill()
                self.argument_list.append(expr)

    def __str__(self):
        string = "("
        for i in range(0, len(self.argument_list)-1):
            string = string + self.argument_list[i].__str__() + ", "
        string = string + self.argument_list[len(self.argument_list)-1].__str__() + ")"
        return string

    def __key__(self):
        types = []
        for a in self.argument_list:
            types.append(a.getType())
        return types.__repr__()

# {[Type] [Name]}*: (int a, float b)
class Parameters(Node):
    def __init__(self, args, data):
        self.__init__(data)
        for a in args.argument_list:
            self.types.append(a.getType())
        self.names = []

    def __init__(self, data):
        Node.__init__(self, data)
        self.types = []
        self.names = []

    def fill(self):
        if (self.data.Handler.check("[")): # list
            while (not self.data.Handler.check("]")):
                Instruction.checkString(self.data, revDict(self.data.all_dict, Type))
                type = findType(self.data, self.data.Handler.next_string())
                self.types.append(type)

                Instruction.checkString(self.data, revDict(self.data.all_dict, Name))
                name = Name(self.data, False)
                name.fill()
                self.names.append(name)

                self.data.Block.add(name.__str__(), Expression(self.data))

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

    def __key__(self):
        return self.types.__repr__()
