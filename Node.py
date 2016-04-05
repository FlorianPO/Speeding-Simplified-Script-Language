# -*- coding: utf-8 -*-

from Exceptions import *
from Plus import *

# Everything is a node which needs to be parse
class Node:
    def __init__(self, data):
        self.node_name = revDict(data.all_dict, self.__class__) # get the right name
        self.data = data
        self.filled = False

    # Parse the node
    def fill(self, check = True):
        pass

    def getName(self):
        return self.node_name
    def __str__(self):
        return "_none_"
    def __repr__(self):
        return self.__str__()