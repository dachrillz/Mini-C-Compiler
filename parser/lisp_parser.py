#import lexer
import ply.yacc as yacc
import operator
from functools import reduce #python 3
import collections

from lexer import tokens



'''
GRAMMAR OF THE LISP!

Program	the start of input, an Operator, one or more Expression, and the end of input.
Expression	: Number | '(' Operator Expression+ ')'.
Operator :	'+' | '-' | '*' | '/'
Number : -?[0-9]+
Symbol:  [^0-9()][^()\ \t\n]*'
'''


#dictionary of names
names = {}  

def p_expr(t): #expression as list!
    '''expression : LPAREN explist RPAREN
                  '''
    if t[2] == None:
        t[0] = ('list', [])
    else:
        t[0] = t[2]


def p_expr_list(t): #This is the renowned S-expression
    ''' explist : expression
                | explist expression
    '''
    if len(t) < 3:
        t[0] = ('list', [t[1]])
    else:
        t[1][1].append(t[2])
        t[0] = t[1]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = ('int', t[1])

def p_expression_symbol(t):
    'expression : SYMBOL'
    t[0] = ('sym',t[1])


def p_empty_paren(t):
    'expression : LPAREN RPAREN'
    t[0] = ('list', '()')
        
def p_error(t):
    if t is None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)
        yacc.errok()


def get_parser():
    return yacc.yacc() 

if __name__ == '__main__':
    parser_instance = yacc.yacc()

    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break

        if not s: continue

        result = parser_instance.parse(s)

        print(result)


