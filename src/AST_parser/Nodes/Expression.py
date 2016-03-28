from Exceptions import *

from Nodes.Node import *

# Expression ________________________________
class Expression(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.value_s = "_none_" # string, literal value

    def fill(self):
        expr = findExpr(self.data)
        self.__class__ = expr.__class__ # change __class__: Expression(4 + 4) -> Add(4, 4)
        self.__dict__.update(expr.__dict__) # copy attributes

    def getType(self):
        raise NotImplementedError("getType interface method, problem...")

class Name(Expression):
    def __init__(self, data, check = True):
        Expression.__init__(self, data)
        self.check = check

    def fill(self):  
        self.value_s = self.data.Handler.next_string()
        if (self.check):
            if (self.data.Block.get(self.value_s) == None):
                self.data.Logger.logError("Error: " + self.value_s + " is not known")
                raise ErrorEnvironment()

    def getType(self):
        return self.data.Block.get(self.value_s)

    def __str__(self):
        return self.value_s

class Value(Expression):
    def __init__(self, data):
        Expression.__init__(self, data)

    def fill(self):
        self.value_s = self.data.Handler.next_string()
    def getType(self):
        return findType(self.data, self.value_s) # find type

    def __str__(self):
        return self.value_s

class Type(Node):
    def __init__(self, data, keyword = None):
        Node.__init__(self, data)
        if (keyword == None):
            self.keyword = "_none_" # int, float, ...
        else:
            self.keyword = keyword

    def fill(self):
        token = self.data.Handler.next_string()
        if (token in self.data.type_list): # check keyword
            self.keyword = token
        else:
            self.data.Logger.logError("Error: " + token + " is not a known type")
            raise ErrorParsing()

    def __str__(self):
        return self.keyword

# Return the true expression object (such as Name, Value, Type, ...)
def findExpr(data):
    if (data.Handler.check("[")): # list
        left_expr = None
        right_expr = None
        operator = None
        
        left_expr = findExpr(data)  
        string = data.Handler.next_string()
        oper = data.all_dict[string](data)
        right_expr = findExpr(data)

        oper.setLeftExpr(left_expr)
        oper.setRightExpr(right_expr)
        
        if (not data.Handler.check("]")):
            self.data.Logger.logError("Error: unable to find end of expression")
            raise ErrorParsing()

        return oper
    else: # single expression
        string = data.Handler.next_string()
        expr = data.all_dict[string](data)
        expr.fill()

        return expr

# Find the best matching type of a given value, ex: 1.5 -> float
def findType(data, string):
    if (string.find('.') >= 0):
        return Type(data, "float")
    return Type(data, "int")