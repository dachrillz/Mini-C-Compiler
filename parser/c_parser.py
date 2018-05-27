#import lexer
import ply.yacc as yacc
import operator
from functools import reduce #python 3
import collections

from lexer import tokens


class AST():
    def traverse_post_order(self, root):
        if root.children is not None:
            if type(root.children) == list:
                for item in root.children:
                    self.traverse_post_order(item)
            else:
                self.traverse_post_order(root.children)

            print(root)

class program_node(AST):
    def __init__(self,statement):
        self.children = statement



class function_node(AST):
    def __init__(self, type_,name,arguments,body):
        self.type = type_
        self.name = name
        self.children = [arguments,body]

    def __repr__(self):
        return "function: " + self.name + "::" + self.type + ', ' + str(self.children[0]) + ', ' + str(self.children[1])
    

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
        return 'statement: ' + str(self.children)

class return_node(AST):
    def __init__(self, statements):
        self.children = statements

    def __repr__(self):
        return 'return: ' + str(self.children)

class arguments_node(AST):
    def __init__(self, statements):
        self.children = statements

    def __repr__(self):
        return 'arg: ' + str(self.children)
        
'''
Minimal Grammar of the C-language

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <int>
'''


#dictionary of names
names = {}

def p_program(t):
    '''program : function'''
    t[0] = program_node(t[1])

def p_function(t):
    '''function : INT IDENTIFIER LPAREN RPAREN LBRACE statement RBRACE'''
    t[0] = function_node(t[1], t[2], arguments_node(None), t[6])

def p_exp(t):
    '''exp : INTEGER'''
    t[0] = constant_node(t[1])


def p_statement(t): #expression as list!
    '''statement : RETURN exp SEMICOLON
                  '''
    t[0] = statement_node(return_node(t[2]))

  
def p_error(t):
    if t is None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)
        yacc.errok()


def get_parser():
    return yacc.yacc() 


def closure(list_to_traverse):
    nodes_visited = []

    def traverse_post_order(list_to_traverse):
        list_to_traverse = list_to_traverse[1]

        for item in reversed(list_to_traverse):
            if type(item[1]) == list:
                traverse_post_order(item)
                print(item)
                nodes_visited.append(item)
            else:
                nodes_visited.append(item)
                print (item)
    
    traverse_post_order(list_to_traverse)
    return nodes_visited

if __name__ == '__main__':
    s = '''int main() {
    return 2;
    }
    '''


    parser_instance = yacc.yacc()

    result = parser_instance.parse(s)

    result.traverse_post_order(result)

