# -*- coding: utf-8 -*-

class Instruction:
    def __init__(self, token_list):
        self.token_expected = token_list
        self.node_list = []

    def token(self, name, token): #"TYPE": "int"
        if token == self.token_expected[0]:
            self.node_list.append(token)
        else:
            print("Erreur, token expected: %s \t got %s" % self.token_expected[0] % token)

class Declaration(Instruction):
    def __init__(self):
        self.nom = "DECL"
        Instruction.__init__(self,  ["TYPE", "EXPR", "EXPR"]) # int a = 4
        


