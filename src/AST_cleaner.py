# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

def main():
    AST = open('full_AST', 'r').read()

    b_inString = False
    i = 0;
    left = 0
    
    only_spaces = True
    erase_line = False
    # TODO if '"' is a program character
    # TODO inline AST
    while (i < len(AST)):
        if (b_inString):
            if (AST[i] == '"'):
                b_inString = False
        else:
            if (AST[i] == '\n'):
                if (only_spaces or erase_line):
                    AST = AST[:left] + AST[i:]
                    i = left
                    erase_line = False
                else:
                    left = i
                only_spaces = True
            elif (AST[i] == ',' or AST[i] == '{' or AST[i] == '}'):
                AST = AST[:i] + " " + AST[i+1:]
            elif (AST[i] == 'n'): # null incoming
                erase_line = True
            elif (AST[i] == '[' and AST[i+1] == ']' and only_spaces):
                erase_line = True
            elif (AST[i] == '"'):
                b_inString = True
                only_spaces = False
            elif (AST[i] != ' '):
                only_spaces = False
        i = i+1

    print(AST)

if __name__ == '__main__':
    main()
