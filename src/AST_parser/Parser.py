# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
from Exceptions import *

from Data import Data
import Go

# Parse the whole AST
def parse(data):
    data.Handler.check("[")
    while (data.Handler.hasNext()): # read lines
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

    data.Logger.log("Begin of parsing...")

    data.Block = data.MainBlock
    parse(data) # main process

    data.Logger.log("End of file...")

    data.Logger.printAllLog()
    print("")
    print("Result:")
    data.Logger.printLogAST()
    print("")
    print("Go")

    Go.init()
    for instr in data.MainBlock.instr_list:
        print(instr.__go__())
    

    # TODO code generation

if __name__ == '__main__':
    main()
