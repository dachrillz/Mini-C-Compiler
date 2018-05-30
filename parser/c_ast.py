'''
This file contains the definitions of the AST that the parser generates.
The AST constists of Python classes, where each class is a node in a tree.

@TODO: Implement a pretty print for the tree structure
'''

    

class AST():
    pass


class program_node(AST):
    def __init__(self,statement):
        self.children = statement



class function_node(AST):
    def __init__(self, type_,name,body):
        self.type = type_
        self.name = name
        self.children = body

    def __repr__(self):
        return "function: " + self.name + "::" + self.type #+ ', ' + str(self.children[0]) + ', ' + str(self.children[1])
    

class constant_node(AST):
    def __init__(self, value):
        self.value = value
        self.children = None

    def __repr__(self):
        return 'constant: ' + str(self.value)

class statement_node(AST):
    def __init__(self, statements):
        self.children = statements

    def __repr__(self):
        return 'statement'

class return_node(statement_node):
    def __init__(self,expression):
        self.children = expression

    def __repr__(self):
        return 'return'

class arguments_node(AST):
    def __init__(self, statements):
        self.children = statements

    def __repr__(self):
        return 'arg: ' + str(self.children)
