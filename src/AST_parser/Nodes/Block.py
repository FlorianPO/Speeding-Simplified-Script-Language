# -*- coding: utf-8 -*-

from Exceptions import *
from Logger import Logger
from Handler import Handler

from Nodes.Node import *

# Define a block of instructions, and so an environment
class Block(Node):
    def __init__(self, parent, data, naede="rien"):
        Node.__init__(self, data)
        self.parent = parent # super environment
        self.instr_list = [] # instructions inside the block
        self._env_dict = {} # variable environment
        self._envFunc_dict = {} # function environment
        self._envClass_dict = {} # class environment

    # Add a variable to environment
    def add(self, name, type):
        if (not name in self._env_dict): # check in current environment
           self._env_dict[name] = type
        else:
            self.data.Logger.logError("Error: " + name + " already exists")
            raise ErrorDeclaration()

    def addAll(self, name, type):
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

    # Add a function to environment
    def addFunction(self, name, param, return_type):
        if (not (name, param) in self._envFunc_dict): # check if it doesn't exist yet
            self._envFunc_dict[(name, param)] = return_type
        else:
            self.data.Logger.logError("Error: " + name + " function already exists")
            raise ErrorDeclaration()

    def addFunctionAll(self, name, param, return_type):
        if (self.getFunction(name, param) == None): # check if it doesn't exist yet
            self._envFunc_dict[(name, param)] = return_type
        else:
            self.data.Logger.logError("Error: " + name + " function already exists")
            raise ErrorDeclaration()

    # Modify a function in environment
    def modifyFunction(self, name, param, return_type):
        if ((name, param) in self._envFunc_dict): # check in current environment
            self._envFunc_dict[(name, param)] = return_type
        elif (self.parent != None): # check in super environment
            self.parent.modifyFunction(name, param, return_type)
        else:
            self.data.Logger.logError("Error: " + name + " function doesn't exist")
            raise ErrorEnvironment()

    # Delete a function in environment
    def deleteFunction(self, name, param):
        if (self.getFunction(name, param) != None): # check if it already exists
            del self._envFunc_dict[(name, param)]
        else:
            self.data.Logger.logError("Error: " + name + param.__str__() + " function doesn't exists")
            raise ErrorDeclaration()

    # Get a function in environment (returns its type)
    def getFunction(self, name, param):
        return_type = None
        if ((name, param) in self._envFunc_dict): # check in current environment
            return_type = self._envFunc_dict[(name, param)]
        elif (self.parent != None): # check in super environment
            return_type = self.parent.getFunction(name, param)

        return return_type

    # Add a class to environment
    def addClass(self, name, _class):
        if (not name in self._envClass_dict): # check if it doesn't exist yet
            self._envClass_dict[name] = _class
        else:
            self.data.Logger.logError("Error: " + name + " class already exists")
            raise ErrorDeclaration()

    def addClassAll(self, name, _class):
        if (self.getClass(name) == None): # check if it doesn't exist yet
            self._envClass_dict[name] = _class
        else:
            self.data.Logger.logError("Error: " + name + " class already exists")
            raise ErrorDeclaration()

    # Modify a class in environment
    def modifyClass(self, name, _class):
        if (name in self._envClass_dict): # check in current environment
            self._envClass_dict[name] = _class
        elif (self.parent != None): # check in super environment
            self.parent.modifyClass(name, _class)
        else:
            self.data.Logger.logError("Error: " + name + " class doesn't exist")
            raise ErrorEnvironment()

    # Delete a class in environment
    def deleteClass(self, name):
        if (self.getClass(name) != None): # check if it already exists
            del self._envClass_dict[name]
        else:
            self.data.Logger.logError("Error: " + name + " class doesn't exists")
            raise ErrorDeclaration()

    # Get a class in environment
    def getClass(self, name):
        _class = None
        if (name in self._envClass_dict): # check in current environment
            _class = self._envClass_dict[name]
        elif (self.parent != None): # check in super environment
            _class = self.parent.getClass(name)

        return _class

    # Return the next instruction
    def nextInstruction(self):
        string = self.data.Handler.next_string()
        if (string == ""):
            raise NoInstructionLeft()
        instr = self.data.instr_dict[string](self.data) # create instruction
        self.instr_list.append(instr)
        return instr

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                self.data.Handler.checkString(self.node_name) # check for the right statement
            if (self.data.Handler.check("[")):
                self.data.Block = self
                while (not self.data.Handler.check("]")):
                    instruction = self.nextInstruction()
                    self.data.Logger.logAST(instruction)
                self.data.Block = self.parent
            self.filled = True

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