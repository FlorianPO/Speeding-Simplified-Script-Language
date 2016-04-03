# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

from Exceptions import *
from Data import *
import Go

# Parse the whole AST
def parse(data):
    data.GlobalBlock.fill()
    
def main():
    f = open('AST', 'r')

    data = Data()
    data.Handler.setAST(f.read()) # Give string to handler

    parse(data)

    data.Logger.printAllLog()
    print("")
    print("Result:")
    for instr in data.GlobalBlock.instr_list:
        print(instr.__str__())
    print("")
    print("Go:")

    Go.init()
    for instr in data.GlobalBlock.instr_list:
        print(instr.__go__())

if __name__ == '__main__':
    main()
