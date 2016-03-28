# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

from Exceptions import *
from Data import *
import Go

# Parse the whole AST
def parse(data):
    # DEFS
    if (data.Handler.next_string() != "DEFS"):
        print("Error, DEFS not found")
    data.GlobalBlock.fill()
    
    # if (data.Handler.next_string() != "MAIN"):
    #     print("Error, MAIN not found")
    # if (data.Handler.next_string() != "PARAM"):
    #     print("Error, PARAM not found")
    # data.Block = data.MainBlock
    # parm = Parameters(data)
    # parm.fill()

    # if (data.Handler.next_string() != "BLOCK"):
    #     print("Error, BLOCK not found")
    # data.MainBlock.fill()

def parseBlock(data):
     if (not data.Handler.check("[")): # list
        self.data.Logger.logError("Error: unable to find begining of block")
        raise ErrorParsing()

     while (not data.Handler.check("]")): # read lines
        try:
            instruction = data.Block.nextInstruction()

            data.Logger.logAST(instruction)
        except NoInstructionLeft:
            break # End of file
        except:
            data.Logger.printAllLog()
            exit()

def main():
    f = open('AST', 'r')

    data = Data()
    data.Handler.setAST(f.read()) # Give string to handler

    parse(data)

    data.Logger.printAllLog()
    print("")
    print("Result:")
    data.Logger.printLogAST()
    print("")
    print("Go:")

    Go.init()
    for instr in data.GlobalBlock.instr_list:
        print(instr.__go__())
    # for instr in data.MainBlock.instr_list:
    #     print(instr.__go__())
    

    # TODO code generation

if __name__ == '__main__':
    main()
