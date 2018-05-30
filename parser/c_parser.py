#import lexer
import ply.yacc as yacc
import operator
from functools import reduce #python 3
import collections

from lexer import tokens

def traverse_post_order(root):
    '''
    @TODO: This function can probably be removed later as its functionality
    was moved to the AST_Visitor class
    '''
    result = []

    def recurse(node):

        if node is None:
            return
        if type(node.children) == list:
            for item in node.children:
                recurse(item)
        else:
            recurse(node.children)

        result.append(node)

    recurse(root)

    return result


class AST_visitor():
    def __init__(self):
        pass


    def generate_code(self, root):
        
        tab = 4 * ' '
        
        post_order_list = self.traverse_AST_post_order(root)
        stack = collections.deque()

        def consume_node(node):
            if isinstance(node, function_node):
                name = node.name
                function_string = '.globl ' + name + '\n' + name + ':'
                stack.appendleft(function_string)

            elif isinstance(node, statement_node):
                if isinstance(node, return_node):
                    value_to_return = stack.popleft()
                    return_string = 'movl' + tab + '$' + str(value_to_return) + ' ,%eax \nret'
                    stack.appendleft(return_string)
                    
                    
            elif isinstance(node, constant_node):
                stack.appendleft(node.value)      

        for node in post_order_list:
            consume_node(node)

        for item in stack:
            print(item)

    
    def traverse_AST_post_order(self,root):
        '''
        @TODO: Look up how it is with generators, if the tree is large, we might not want to 
        load the full tree into memory
        '''
        result = []

        def recurse(node):
            if node is None:
                return
            if type(node.children) == list:
                for item in node.children:
                    recurse(item)
            else:
                recurse(node.children)

            #@TODO: rewrite so that this function is capable of directly calling the consume method in this class.
            result.append(node)

        recurse(root)

        return result


    

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
    t[0] = function_node(t[1], t[2], t[6])

def p_exp(t):
    '''exp : INTEGER'''
    t[0] = constant_node(t[1])


def p_statement(t): #expression as list!
    '''statement : RETURN exp SEMICOLON
                  '''
    t[0] = return_node(t[2])

  
def p_error(t):
    if t is None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)
        yacc.errok()


def get_parser():
    return yacc.yacc() 


if __name__ == '__main__':
    import sys
    file_to_compile = sys.stdin.readlines()

    file_to_compile = ''.join(file_to_compile)

    parser_instance = yacc.yacc()

    result = parser_instance.parse(file_to_compile)

    #traverse_post_order(result)

    AST_i = AST_visitor()

    AST_i.generate_code(result)