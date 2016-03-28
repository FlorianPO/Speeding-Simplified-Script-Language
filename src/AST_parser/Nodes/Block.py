from Exceptions import *
from Logger import Logger
from Handler import Handler

from Nodes.Node import *

# Define a block of instructions, and so an environment
class Block(Node):
    def __init__(self, parent, data):
        Node.__init__(self, data)
        self.parent = parent
        self.instr_list = [] # instructions inside the block
        self.env_dict = {}
        self.envFunc_dict = {}

    def setParentEnv(self, parent):
        self.parent = parent

    def add(self, name, expr):
        if (self.get(name) == None):
            self.env_dict[name] = expr
        else:
            self.data.Logger.logError("Error: " + name + " already exists")
            raise ErrorDeclaration()

    def modify(self, name, expr):
        if (name in self.env_dict):
            self.env_dict[name] = expr
        elif (self.parent != None):
            self.parent.modify(name, expr)
        else:
            self.data.Logger.logError("Error: " + name + " doesn't exist")
            raise ErrorEnvironment()

    def delete(self, name):
        if (self.get(name) != None):
            del self.env_dict[name]
        else:
            self.data.Logger.logError("Error: " + name + " doesn't exists")
            raise ErrorDeclaration()

    def get(self, name):
        value = None
        if (name in self.env_dict):
            value = self.env_dict[name]
        elif (self.parent != None):
            value = self.parent.get(name)

        return value

    def addFunction(self, name, types, block):
        if (self.getFunction(name, types) == None):
            self.envFunc_dict[(name, types)] = block
        else:
            self.data.Logger.logError("Error: " + name + " function already exists")
            raise ErrorDeclaration()

    def modifyFunction(self, name, types, block):
        if ((name, types) in self.envFunc_dict):
            self.envFunc_dict[(name, types)] = block
        elif (self.parent != None):
            self.parent.modifyFunction(name, types, block)
        else:
            self.data.Logger.logError("Error: " + name + " function doesn't exist")
            raise ErrorEnvironment()

    def deleteFunction(self, name, types):
        if (self.getFunction(name, types) != None):
            del self.envFunc_dict[(name, types)]
        else:
            self.data.Logger.logError("Error: " + name + types.__str__() + " function doesn't exists")
            raise ErrorDeclaration()

    def getFunction(self, name, types):
        block = None
        if ((name, types) in self.envFunc_dict):
            block = self.envFunc_dict[(name, types)]
        elif (self.parent != None):
            block = self.parent.getFunction(name, types)

        return block

    # Return the next line ("DECL", ...)
    def nextInstruction(self):
        string = self.data.Handler.next_string()

        if (string == ""):
            raise NoInstructionLeft()
        instr = Instruction.create(string, self.data) # create instruction node
        self.instr_list.append(instr)
        return instr

    def fill(self):
        self.data.Block = self
        if (self.data.Handler.check("[")): # list
            while (not self.data.Handler.check("]")): # read lines
                instruction = self.data.Block.nextInstruction()
                self.data.Logger.logAST(instruction)

        self.data.Block = self.parent

    def __str__(self):
        _size = len(self.instr_list)

        if (_size == 0):
            return "{}"

        string = "{ "
        for i in range(0, _size-1):
            string = string + self.instr_list[i].__str__() + " "
        string = string + self.instr_list[_size-1].__str__()
        string = string + " } "

        return string