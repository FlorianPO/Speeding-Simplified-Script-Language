# -*- coding: utf-8 -*-

from Exceptions import *
from Plus import *

# Everything is a node which needs to be parse
class Node:
    def __init__(self, data):
        self.node_name = revDict(data.all_dict, self.__class__) # get the right name
        self.data = data

    # Parse the node
    def fill(self): # pure virtual
        raise NotImplementedError("fill interface method, problem...")

    def getName(self):
        return self.node_name
    def __str__(self):
        return "_none_"
    def __repr__(self):
        return self.__str__()

# An instruction is a list of nodes which need to be parse
# Using this class automates the parsing process
class Instruction(Node):
    # _STATIC_ returns an instance if the right object to a given string
    def create(string, data):
        return data.instr_dict[string](data)

    # _STATIC_ check if the next statement is equal to string
    def checkString(data, string):
        token = data.Handler.next_string()
        if (not (token == string)):
            data.Logger.logError("Error, unable to match token " + token)
            raise ErrorParsing()

    def __init__(self, token_list):
        self.tokens = token_list # list of tokens expected for instruction
        self._tokens_index = 0 # token list index
        self.fill()

    def fill(self):
        while (not self.isComplete()): # fill nodes
            self.checkToken() # OPTIONAL _/ ! \_ AST could become smaller
            self.tokens[self._tokens_index].fill()

            self._tokens_index += 1

    # Check if the token corresponds to the expected tokens
    def checkToken(self):
        token = self.data.Handler.next_string()
        if (not (token == self.tokens[self._tokens_index].getName())):
            self.data.Logger.logError("Error, unable to match token "+  token + " in discoverToken, waiting for " + self.tokens[self._tokens_index].getName())
            raise ErrorParsing()

    # Returns True if all nodes have been parsed
    def isComplete(self):
        return (self._tokens_index >= len(self.tokens))

    def __str__(self):
        return self.node_name.__str__() + ": " + self.tokens.__str__()