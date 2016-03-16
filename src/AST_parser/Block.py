from Logger import Logger
from Handler import Handler

from Exceptions import NoInstructionLeft
from Exceptions import ErrorParsing

class Block:
    def __init__(self, parent = None):
        self.string_listed = None
        self.parent = parent # super environment
        self.instr_list = [] # instructions inside the block

    def setParentEnv(parent):
        self.parent = parent

    # Return the next line ("DECL", ...)
    def next_line(self):
        string = Handler._s.next_string()

        if (string == ""):
            raise NoInstructionLeft()

        if (self.string_listed == None):
            if (Handler._s.check('[')):
                self.string_listed = string
        else:
             if (Handler._s.check(']')):
                self.string_listed = None
                self.next_line() # repeat process

        return string

    def _list_line(self, string):
        while not Handler._s.check("]"):
            Handler._s.next_string()
            expr_dict.get(string)


# _g: contains global variables, could also contains some initialisation instructions
class GlobalEnv():
    _s = Block() # global environment

 # _m: main block
class MainBlock():
    _s = Block(GlobalEnv._s) # main
    
