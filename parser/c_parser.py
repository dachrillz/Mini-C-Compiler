import ply.yacc as yacc
from c_ast import *
from lexer import tokens
        
'''
Minimal Grammar of the C-language

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <int>
'''


'''
Python implementation of the grammar
'''
def p_program(t):
    '''program : function'''
    t[0] = program_node(t[1])

def p_function(t):
    '''function : INT IDENTIFIER LPAREN RPAREN LBRACE statement RBRACE'''
    t[0] = function_node(t[1], t[2], t[6])

def p_exp(t):
    '''exp : INTEGER'''
    t[0] = constant_node(t[1])


def p_statement(t):
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
    '''
    For manual testing
    '''
    import sys
    file_to_compile = sys.stdin.readlines()

    file_to_compile = ''.join(file_to_compile)

    parser_instance = yacc.yacc()

    result = parser_instance.parse(file_to_compile)
