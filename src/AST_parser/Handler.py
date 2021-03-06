﻿# -*- coding: utf-8 -*-

from Exceptions import *
from Logger import Logger

# Program parser
class Handler:
    ignore_list = [' ', ',', ':', '{', '}', '\n', '\t']
    # Return True if the character is useless
    def ignore(c):
        return (c in Handler.ignore_list) 

    def __init__(self, name, logger):
        self.logger = logger
        self.name = name
        self.AST = "_none_" # the whole SSSL program
        self.i = None # index in string

    def setAST(self, AST):
        self.AST = AST
        self.setIndex()

    def setIndex(self, i=0):
        self.i = i

    def next(self): # retrieve next character
        self.i += 1
        return self.AST[self.i-1]

    def nextTest(self): # retrieve next character without consuming it
         return self.AST[self.i]

    def hasNext(self): # not EOF
        return (self.i < len(self.AST))

    # Return the next string (returns "" when end of file)
    def next_string(self):
        while (self.hasNext()):
            c = self.next()
            if (c == '"'):
                break

        string = ""
        while (self.hasNext()):
            c = self.next()
            if (c == '"'):
                if (len(string) > 0):
                    break
                continue
            string += c

        if (string != ""):
            self.logger.log("-> " + string)
        return string

    # Check the next character with string, else handler is unchanged 
    def check(self, string, restore=False):
        i = self.i # save state
        while (self.hasNext()):
            c = self.next()
            if (c == string[0]):
                if (restore):
                    self.i = i # restore state
                return True
            if (Handler.ignore(c)):
                continue
            else:
                self.i = i # restore state
                return False

    # check if the next statement is equal to string
    def checkString(self, string):
        token = self.next_string()
        if (not (token == string)):
            self.logger.logError("Error, unable to match " + string + " and token " + token)
            raise ErrorParsing()