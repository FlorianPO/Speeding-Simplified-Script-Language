# Variables

class Variable:
	def __init__(self, nom):
		self.nom = nom

class Single:
	def __init__(self, valeur):
		self.valeur = valeur

class Type:
	def __init__(self, type):
		self.type = type

class Num(Variable, Single, Type):
	def __init__(self, nom, valeur, type):
		Variable.__init__(self,  nom)
		Single.__init__(self, valeur)
		Type.__init__(self, type)

class Cst(Single, Type):
	def __init__(self, valeur, type):
		Single.__init__(self, valeur)
		Type.__init__(self, type)

# Expressions

class Expression:
	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

class Add(Expression): # expr1 + expr2
	def __init__(self, expr1, expr2):
		Expression.__init__(self, expr1, expr2)

class Sub(Expression): # expr1 - expr2
	def __init__(self, expr1, expr2):
		Expression.__init__(self, expr1, expr2)

class Mul(Expression): # expr1 * expr2
	def __init__(self, expr1, expr2):
		Expression.__init__(self, expr1, expr2)

class Div(Expression): # expr1 / expr2
	def __init__(self, expr1, expr2):
		Expression.__init__(self, expr1, expr2)

# Store / Load / Del
		
# # String
# class String:
# 	def __init__(self, nom, valeur):
# 		self.nom = 'mon_string_ficelle'
# 		self.valeur = '4 euros'
		
# # List - TRICKY
# class List:
# 	def __init__(self, nom, valeur):
# 		self.nom = 'ma_liste'
# 		self.valeur = '4 euros'
		
# # Hashmap - MACHIN

# # Class
# class Class:
# 	def __init__(self, nom, valeur):
# 		#
# 		#
