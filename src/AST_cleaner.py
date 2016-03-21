# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

def main():
    AST = open('full_AST', 'r').read()

    b_inString = False
    i = 0;
    left = 0
    right = 0
    # TODO if '"' is a program character
    # TODO inline AST
    while (i < len(AST)):
        if (b_inString):
            if (AST[i] == '"'):
                b_inString = False
        else:
            if (AST[i] == '\n'):
                left = i
            elif (AST[i] == ','):
                AST = AST[:i] + " " + AST[i+1:]
            elif (AST[i] == '"'):
                b_inString = True
            elif (AST[i] == 'n' or (AST[i] == '[' and AST[i+1] == ']')): # null incoming
                while (AST[i] != '\n'):
                    i = i+1
                right = i
                AST = AST[:left] + AST[right:]
                i = left
        i = i+1

    print(AST)

if __name__ == '__main__':
    main()
