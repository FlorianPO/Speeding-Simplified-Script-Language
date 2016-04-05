from Exceptions import *

from Nodes.Node import *

# Abstract class of an expression
# You can create an expression that will specialize itself into a child-class object
class Expression(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.value_s = "_none_" # string, literal value

    def fill(self, check = True):
        if (not self.filled):
            _previous_class = self.data._class
            self.data._class = None
            if (check):
                self.data.Handler.checkString(revDict(self.data.all_dict, self.__class__)) # check for Expression statement
            expr = findExpr(self.data)
            self.data._class = _previous_class
            self.__class__ = expr.__class__ # change __class__: Expression(4 + 4) -> Add(4, 4)
            self.__dict__.update(expr.__dict__) # copy attributes
            self.filled = True

    def getType(self):
        raise NotImplementedError("getType interface method, problem...")

# Defines a variable or function name
class Name(Expression):
    def __init__(self, data, check = True):
        Expression.__init__(self, data)
        self._check = check # check in environment or not
        self._type = None

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                self.data.Handler.checkString(self.node_name) # check for the right statement
            self.value_s = self.data.Handler.next_string()
            if (self._check and self.data.check_environment): # check environment
                _class = self.data.Block.getClass(self.data._class.__str__())
                if (_class != None):
                    self._type = _class.get(self.value_s)
                    if (self._type == None):
                        self.data.Logger.logError("Error: " + self.value_s + " is not known in class " + self.data._class.__str__())
                        raise ErrorEnvironment()
                else:
                    self._type = self.data.Block.get(self.value_s)
                    if (self._type == None):
                        self.data.Logger.logError("Error: " + self.value_s + " is not known")
                        raise ErrorEnvironment()
            self.filled = True

    def getType(self):
        return self._type

    def __str__(self):
        return self.value_s

# Defines a immediate value
class Value(Expression):
    def __init__(self, data):
        Expression.__init__(self, data)

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                self.data.Handler.checkString(self.node_name) # check for the right statement
            self.value_s = self.data.Handler.next_string()
            self.filled = True

    def getType(self):
        return findType(self.data, self.value_s) # find type

    def __str__(self):
        return self.value_s



# Defines a type
class Type(Node):
    def __init__(self, data, keyword = None):
        Node.__init__(self, data)
        if (keyword == None):
            self.keyword = "_none_" # int, float, ...
        else:
            self.keyword = keyword
            self.filled = True

    def fill(self, check = True):
        if (not self.filled):
            if (check):
                self.data.Handler.checkString(self.node_name) # check for the right statement
            token = self.data.Handler.next_string()
            if (self.data.check_type):
                if (not(token in self.data.type_list or self.data.Block.getClass(token) != None)): # check keyword
                    self.data.Logger.logError("Error: " + token + " is not a known type or class")
                    raise ErrorParsing()
            self.keyword = token
            self.filled = True

    def __str__(self):
        return self.keyword

# Return the true expression object (such as Name, Value, Type, ...)
def findExpr(data):
    if (data.Handler.check("[")): # operator present
        left_expr = findExpr(data)
        right_expr = None
        oper = None
        while (not data.Handler.check("]")):
            string = data.Handler.next_string()
            oper = data.all_dict[string](data)
            
            right_expr = findExpr(data)

            oper.setExpr(left_expr, right_expr)
            left_expr = oper
        return oper
    else: # single expression
        string = data.Handler.next_string()
        expr = data.all_dict[string](data)
        expr.fill(False)
        data._class = expr.getType() # save class if an access occures

        return expr

# Find the best matching type of a given value, ex: 1.5 -> float
def findType(data, string):
    if (string.find('.') >= 0):
        return Type(data, "float")
    elif (string.find("'") >=0):
        return Type(data, "string")
    return Type(data, "int")
