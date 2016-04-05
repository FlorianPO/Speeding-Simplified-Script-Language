from Exceptions import *

from Nodes.Node import *
from Nodes.Expression import *

class Echo(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.expr = Expression(data)
        self.expr.fill()

    def __str__(self):
        return "echo " + self.expr.__str__() + ";"

class Echoln(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.expr = Expression(data)
        self.expr.fill()

    def __str__(self):
        return "echoln " + self.expr.__str__() + ";"