# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import json

import Instructions

import fileinput

# Return True if a character is useless
def ignore(c):
    if c == ' ' or c == '\n' or c == ':':
        return True
    return False 

def eat(string, H):
    i=0
    while H.hasNext():
        c = H.next()
        if (c != string[i]):
            print("Impossible de consommer le caractère %s" % c)
            exit()
        i+=1
        if i >= len(string):
            break

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


# Return the following string
def parse_string(H):
    while H.hasNext():
        c = next()
        if ignore(c):   
            continue
        if c == '"':
            break

    string = ""
    while H.hasNext():
        c = next()
        if c == '"':
            if len(string > 0):
                break
            continue
        string += c

    return string

# Parse the whole AST
def parse(H):
    while H.hasNext():
        string = parse_string(H)
        create_instruction(string, H)

def create_instruction(string, H):
    eat(": ", H)

    bool = False
    if find("[", H):
        bool = True
    else:
        find("{", H)

    while True:
        if string == "DECL":
            node_list.append(Declaration())
        
        while not find("}", H):
            string = parse_string(H)
            # eat(": ", H)
            # if find("[", H):
            #TODO
        if not bool:
            break

node_list = []

def main():
    f = open('AST.txt', 'r')

    H = Handler(f.read())
    parse(H)

if __name__ == '__main__':
    main()

class Handler:
    def __init__(self, string, i=0):
        self.AST = string;
        self.i = i;
        self.node_list = []

    def next(self):
        self.i += 1
        return self.AST[self.i-1]

    def hasNext(self):
        return self.i < len(self.AST)
