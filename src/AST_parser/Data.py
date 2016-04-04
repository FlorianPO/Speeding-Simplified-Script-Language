# -*- coding: utf-8 -*-

from Logger import Logger
from Handler import Handler

from Nodes.Instruction import *
from Nodes.Expression import *
from Nodes.Function import *
from Nodes.Condition import *
from Nodes.Operator import *
from Nodes.Object import *
from Nodes.Block import *

# Parsing data
class Data:
    def __init__(self):
        # LISTS ___________________________________
        self.instr_dict = {"DECL": Declaration, "AFF": Affectation, "DECLAFF": Declaffectation, 
                           "DFUNC": FunctionDef, "CFUNC": FunctionCall,
                           "IF": If, "ELSE": Else, "ELIF": Elif, "WHILE": While, "DOWHILE": DoWhile,
                           "DOBJT": ClassDef, "CSTR": ConstructorDef,
                           "RETURN": Return, "BREAK": Break}

        self.type_list = ["int", "float", "string", "void"]
        self.expr_dict = {"EXPR": Expression, "TYPE": Type, "NAME": Name, "VAL": Value}
        self.oper_dict = {"+": Add, "-": Sub, "*": Mul, "/": Div, ".": Access, "==": Equal, "!=": NEqual}
        self.other_dict = {"PARAM": Parameters, "ARGS": Arguments, "BLOCK": Block}

        self.all_dict = {}
        for d in [self.instr_dict, self.expr_dict, self.oper_dict, self.other_dict]:
            self.all_dict.update(d)

        # CONTENT ___________________________________
        self.Logger = Logger("Default logger")
        self.Handler = Handler("Default handler", self.Logger)
        self.GlobalBlock = Block(None, self, "GLo")
        self.Block = None # current parsing block
        self._class = None
