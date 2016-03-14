# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

from Exceptions import NoInstructionLeft
from Exceptions import ErrorParsing
from Exceptions import Logger

import Instructions

# Return True if the character is useless
ignore_list = [' ', '\n', ':']
def ignore(c):
    return (c in ignore_list) 

# Return the next string
def next_string(H):
    while H.hasNext():
        c = H.next()
        if ignore(c):   
            continue
        if c == '"':
            break

    string = ""
    while H.hasNext():
        c = H.next()
        if c == '"':
            if len(string) > 0:
                break
            continue
        string += c

    Logger._s.log("-> " + string)
    return string

# Consume the given string
def eat(string, H):
    i=0
    while H.hasNext():
        c = H.next()
        if (c != string[i]):
            Logger._s.log("Impossible to consume character " + c + " in string " + string, 1)
            raise ErrorParsing()
        i+=1
        if i >= len(string):
            break

# Check the next character with string, else handler is unchanged 
def check(string, H):
    i = H.i # save state
    while H.hasNext():
        c = H.next()
        if (c == string[0]):
            return True
        if (c == ignore):
            continue
        else:
            H.i = i # restore state
            return False

# Find the next occurence of a character if possible, else handler is unchanged 
def find(string, H):
    i = H.i # save state
    while H.hasNext():
        c = H.next()
        if (c == string[0]):
            return True
        if (c == ignore):
            continue
        else:
            H.i = i # restore state
            return False

# ___________________________________________________

node_list = []
def create_instruction(string, H):
    global instr_dict

    instruction = instr_dict[string]()
    node_list.append(instruction)
    
    while (not instruction.isComplete()): # feed instruction
        instruction.discoverToken(next_string(H))
        instruction.feedToken(next_string(H))


# ___________________________________________________

# Parse the whole AST
def parse(H):
    Logger._s.log("Begin of parsing...")

    string = "_none_"
    while H.hasNext(): # main loop
        try:
            string = next_instruction(H)
            create_instruction(string, H)
        except NoInstructionLeft:
            break # End of file
        except ErrorParsing:
            Logger._s.printLog()
            exit()

    Logger._s.log("End of file...")
    Logger._s.printLog()
    # TODO code generation

first_call = True
instruction_lister = None
# Return the next instruction ("DECL", ...)
def next_instruction(H):
    global first_call
    global instruction_lister

    string = "_none_"

    if ((not first_call) and (not check(",", H))):
        raise NoInstructionLeft()

    if (instruction_lister == None):
        string = next_string(H)
        eat(": ", H)
        if (H.next() == "["): # list
            instruction_lister = Lister(string)
    else:
        if (check(",", H)):
            string = instruction_lister.name
        elif (check("]", H)):
            instruction_lister = None
            string = next_instruction(H) # restart process
        else:
            Logger._s.log("Impossible to find the next token in list or end of list", 1)
            raise ErrorParsing()

    first_call = False
    return string

# Program parser
class Handler:
    def __init__(self, string, i=0):
        self.AST = string; # the whole SSSL program
        self.i = i; # index in string
        self.node_list = [] # abstract tree

    def next(self): # retrieve next character
        self.i += 1
        return self.AST[self.i-1]

    def nextTest(self): # retrieve next character without consuming it
         return self.AST[self.i]

    def hasNext(self): # not EOF
        return self.i < len(self.AST)

class Lister:
    def __init__(self, name):
        self.name = name

def main():
    f = open('AST.txt', 'r')

    H = Handler(f.read())
    parse(H)

if __name__ == '__main__':
    main()
