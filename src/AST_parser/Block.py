from Exceptions import *
import Instructions # circular import

from Logger import Logger
from Handler import Handler

# Define a block of instructions, and so an environment
class Block:
    def __init__(self, parent, data):
        self.data = data
        self.instr_list = [] # instructions inside the block
        self.env_dict = {}
        self.setParentEnv(parent) # super environment

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

    def get(self, name):
        value = None
        if (name in self.env_dict):
            value = self.env_dict[name]
        elif (self.parent != None):
            value = self.parent.get(name)

        return value

    # Return the next line ("DECL", ...)
    def nextInstruction(self):
        string = self.data.Handler.next_string()

        if (string == ""):
            raise NoInstructionLeft()

        instr = Instructions.Instruction.create(string, self.data) # create instruction node
        
        self.instr_list.append(instr)
        return instr
