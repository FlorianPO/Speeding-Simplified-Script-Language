# -*- coding: utf-8 -*-

from Exceptions import *

from Nodes.Node import *
from Nodes.Block import *
from Nodes.Expression import *

# [Type] [Name]: int variable
class Declaration(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.type = Type(data)
        self.name = Name(data, False)

        self.type.fill()
        self.name.fill()

        data.Block.add(self.name.__str__(), self.type) # add variable to environment

    def __str__(self):
        return self.type.__str__() + " " + self.name.__str__() + ";"

# [Type] [Name] [Expr]: int variable = 8
class Declaffectation(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.type = Type(data)
        self.name = Name(data, False)
        self.expr = Expression(data)
        
        self.type.fill()
        self.name.fill()
        self.expr.fill()
        
        if (data.check_type_compability):
            if (self.type.__str__() != self.expr.getType().__str__()): # test type compability
                data.Logger.logError("Error: " + self.type.__str__() + " and " + self.expr.getType().__str__() + " are not compatible")
                raise ErrorType()

        data.Block.add(self.name.__str__(), self.type) # add variable to environment

    def __str__(self):
        return self.type.__str__() + " " + self.name.__str__() + ":=" + self.expr.__str__() + ";"

# [Name] [Expr]: variable = 7
class Affectation(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.name = Name(data, False)
        self.expr = Expression(data)
        
        self.name.fill()
        self.expr.fill()

        if (data.check_environment):
            if (data.Block.get(self.name.__str__()) == None): # test if variable exists in environment
                data.Logger.logError("Error: " + self.name.__str__() + " is not known")
                raise ErrorEnvironment()

        if (data.check_type_compability):
            if (data.Block.get(self.name.__str__()).__str__() != self.expr.getType().__str__()): # test type compability
                data.Logger.logError("Error: " + data.Block.get(self.name.__str__()).__str__() + " and " + self.expr.getType().__str__() + " are not compatible")
                raise ErrorType()

        data.Block.modify(self.name.__str__(), self.expr.getType()) # modify variable in environment

    def __str__(self):
        return self.name.__str__() + "=" + self.expr.__str__() + ";"

class Return(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = None

        if (data.Handler.check("[")):
            if (not data.Handler.check("]")):
                self.data.Logger.logError("Error: unable to find end")
                raise ErrorParsing()
        else:
            self.expr = Expression(data)
            self.expr.fill()

    def __str__(self):
        if (self.expr == None):
            return "return;"
        else:
            return "return " + self.expr.__str__() + ";"

class Break(Node):
    def __init__(self, data):
        Node.__init__(self, data)

        self.expr = ""

        if (not data.Handler.check("[")):
            self.data.Logger.logError("Error: unable to find begining")
            raise ErrorParsing()
        if (not data.Handler.check("]")):
            self.data.Logger.logError("Error: unable to find end")
            raise ErrorParsing()

    def __str__(self):
        return "break;"