# -*- coding: utf-8 -*-

from Exceptions import *
from Logger import Logger
from Handler import Handler

from Nodes.Node import *

# Define a block of instructions, and so an environment
class Block(Node):
    def __init__(self, parent, data):
        Node.__init__(self, data)
        self.parent = parent # super environment
        self.instr_list = [] # instructions inside the block
        self._env_dict = {} # variable environment
        self._envFunc_dict = {} # function environment

    def setParentEnv(self, parent):
        self.parent = parent

    # Add a variable to environment
    def add(self, name, type): 
        if (self.get(name) == None): # check if it doesn't exist yet
            self._env_dict[name] = type
        else:
            self.data.Logger.logError("Error: " + name + " already exists")
            raise ErrorDeclaration()

    # Modify a variable in environment
    def modify(self, name, type):
        if (name in self._env_dict): # check in current environment
            self._env_dict[name] = type
        elif (self.parent != None): # check in super environment
            self.parent.modify(name, type)
        else:
            self.data.Logger.logError("Error: " + name + " doesn't exist")
            raise ErrorEnvironment()

    # Delete a variable in environment
    def delete(self, name):
        if (self.get(name) != None): # check if it already exists
            del self._env_dict[name]
        else:
            self.data.Logger.logError("Error: " + name + " doesn't exists")
            raise ErrorDeclaration()

    # Get a variable in environment (returns its type)
    def get(self, name): 
        value = None
        if (name in self._env_dict): # check in current environment
            value = self._env_dict[name]
        elif (self.parent != None): # check in super environment
            value = self.parent.get(name)

        return value

    # Add a variable to environment
    def addFunction(self, name, types, block):
        if (self.getFunction(name, types) == None): # check if it doesn't exist yet
            self._envFunc_dict[(name, types)] = block
        else:
            self.data.Logger.logError("Error: " + name + " function already exists")
            raise ErrorDeclaration()

    # Modify a function in environment
    def modifyFunction(self, name, types, block):
        if ((name, types) in self._envFunc_dict): # check in current environment
            self._envFunc_dict[(name, types)] = block
        elif (self.parent != None): # check in super environment
            self.parent.modifyFunction(name, types, block)
        else:
            self.data.Logger.logError("Error: " + name + " function doesn't exist")
            raise ErrorEnvironment()

    # Delete a variable in environment
    def deleteFunction(self, name, types):
        if (self.getFunction(name, types) != None): # check if it already exists
            del self._envFunc_dict[(name, types)]
        else:
            self.data.Logger.logError("Error: " + name + types.__str__() + " function doesn't exists")
            raise ErrorDeclaration()

    # Get a function in environment (returns its type)
    def getFunction(self, name, types):
        block = None
        if ((name, types) in self._envFunc_dict): # check in current environment
            block = self._envFunc_dict[(name, types)]
        elif (self.parent != None): # check in super environment
            block = self.parent.getFunction(name, types)

        return block

    # Return the next instruction
    def nextInstruction(self):
        string = self.data.Handler.next_string()
        if (string == ""):
            raise NoInstructionLeft()
        instr = Instruction.create(string, self.data) # create instruction node
        self.instr_list.append(instr)
        return instr

    def fill(self):
        self.data.Block = self # set current environment
        if (self.data.Handler.check("[")):
            while (not self.data.Handler.check("]")):
                instruction = self.data.Block.nextInstruction()
                self.data.Logger.logAST(instruction)

        self.data.Block = self.parent # retrieve old environment

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