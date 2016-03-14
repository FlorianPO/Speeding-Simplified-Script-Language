# -*- coding: utf-8 -*-

type_list = ["int", "float"] # TODO complete
# Check if the given string match a type keyword such as "int"
def isTypeKeyword(string):
    return (string in type_list)

# Check if a name var exists in the environment (return true if valid)
def checkEnv(string):
    # TODO
    return

# Find the best matching type of a given value, ex: 1.5 -> float
def findType(string):
    # TODO
    return

expr_dict = {"TYPE": Type.__class__, "NAME": Name.__class__, "VALUE" : Value.__class__}
# Return the true expression object (such as Name, Value, Type, ...)
def findExpr(string):
    class_name = expr_dict.get(string)
   
    # TODO recursive calls -> where all is performed
    return class_name

# NODE ____________________________________
class Node:
    def __init__(self):
        self.node_name

    def isTerminal(self): # pure virtual
        raise NotImplementedError("isTerminal interface method, problem...")

    def feedMe(self, token): # pure virtual
        raise NotImplementedError("feedMe interface method, problem...")

    def getName(self):
        return self.node_name

class Terminal(Node):
    def __init__(self):
        pass

    def isTerminal(self):
        return True

class nonTerminal(Node):
    def __init__(self):
        pass
    
    def isTerminal(self):
        return False

# NON TERMINAL ____________________________
class Instruction(nonTerminal):
    def __init__(self, token_list):
        self.tokens = token_list
        self.discovered_token

    def discoverToken(self, token):
        if (token in self.tokens):
            self.discovered_token = self.tokens[self.tokens.index(token)]
            self.tokens.remove(self.tokens.index(token))
        else:
            print("Error, unable to match a token")
            exit()

    def feedToken(self, token):
        self.discovered_token.feedMe(token)

    def isComplete(self):
        return self.tokens.size() == 0

class Declaration(Instruction):
    def __init__(self):
        self.node_name = "DECL"
        Instruction.__init__(self,  [Type(), Name(), Expression()]) # int a = 4

# UNDEFINED _______________________________
class Arguments(Instruction):
    pass # TODO

# TERMINAL ________________________________
class Expression(Terminal):
    def __init__(self):
        self.node_name = "EXPR"

    def feedMe(self, token):
        self.__class__ = findExpr(token) # WARNING: this may not work

class Type(Expression):
    def __init__(self):
        self.keyword = ""
        self.node_name = "TYPE"

    def feedMe(self, token):
        if (isTypeKeyword(token)): # check keyword
            self.keyword = token
        else:
            print("Error, %s is not a known type" % token)
            exit()

class Name(Expression):
    def __init__(self, b_decl = False):
        self.name = ""
        self.decl = b_decl;
        self.node_name = "NAME"

    def feedMe(self, token):
        if (not self.decl): # check environment
            if (not checkEnv(token)):
                print("Error, %s is not known" % token)
                exit()
        self.name = token

class Value(Expression):
    def __init__(self):
        self.val = "";
        self.type; # type of type_list ("int", "float", ...)
        self.node_name = "VAL"

    def feedMe(self, token):
        self.type = findType(token) # find type
        self.val = token
