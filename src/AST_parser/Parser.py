# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import fileinput

from Exceptions import NoInstructionLeft
from Exceptions import ErrorParsing
from Logger import Logger

from Block import MainBlock
from Handler import Handler

from Instructions import Instruction

# Parse the whole AST
def parse(current_block):
    while (Handler._s.hasNext()): # read lines
        try:
            string = current_block.next_line()
            create_instruction(string)
        except NoInstructionLeft:
            break # End of file
        except ErrorParsing:
            Logger._s.printAllLog()
            exit()

def create_instruction(string):
    global instr_dict

    instruction = Instruction.create(string) # Create instrucion node
    instruction.fill()
      
    Logger._s.logAST(instruction)

def main():
    f = open('AST.txt', 'r')

    Handler._s.setAST(f.read()) # Give string to handler

    Logger._s.log("Begin of parsing...")
    parse(MainBlock._s) # main process
    Logger._s.log("End of file...")

    Logger._s.printLogAST()
    print("")
    Logger._s.printAllLog()
    print("")

    # TODO code generation

if __name__ == '__main__':
    main()
