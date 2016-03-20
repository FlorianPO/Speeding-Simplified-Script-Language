from Logger import Logger
from Block import Block
from Handler import Handler

from Instructions import *

class Data:
    def __init__(self):
        self.Logger = Logger("Default logger")
        self.Handler = Handler("Default handler", self.Logger)
        self.GlobalBlock = Block(None, self)
        self.MainBlock = Block(self.GlobalBlock, self)
        self.Block = None # current block

        # LISTS ___________________________________
        self.instr_dict = {"DECL": Declaration, "AFFECT": Affectation} # TODO complete
        self.type_list = ["int", "float"] # TODO complete
        self.expr_dict = {"EXPR" : Expression, "TYPE": Type, "NAME": Name, "VAL" : Value} # TODO complete
        self.oper_dict = {"+" : Add, "-": Sub, "*": Mul, "/" : Div} # TODO complete

        self.all_dict = {}
        for d in [self.instr_dict, self.expr_dict, self.oper_dict]:
            self.all_dict.update(d)

        self.type_compability = []
        self.type_compability.append(["int", "float"])
