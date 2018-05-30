import ply.yacc as yacc
from c_ast import *
from lexer import tokens
        
'''
Minimal Grammar of the C-language

<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <unary_exp> <exp> | <int>
'''

precedence = (
    ('right', 'UNARY_OP'),            # Unary minus operator
)

'''
Python implementation of the grammar
'''
def p_program(t):
    '''program : function'''
    t[0] = program_node(t[1])

def p_function(t):
    '''function : INT IDENTIFIER LPAREN RPAREN LBRACE statement RBRACE'''
    t[0] = function_node(t[1], t[2], t[6])


def p_unary_op(t):
    '''unary_op : NEGATION exp 
                | BITWISE_COMPLEMENT exp
                | LOGICAL_NEGATION exp'''

    t[0] = unary_node(t[1], constant_node(t[2]))

def p_exp(t):
    '''exp : unary_op %prec UNARY_OP
           | INTEGER'''

    t[0] = t[1]

def p_statement(t):
    '''statement : RETURN exp SEMICOLON
                  '''
    t[0] = return_node(t[2])

  
def p_error(t):
    if t is None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)
    parser_instance.errok()


def get_parser():
    return yacc.yacc() 


if __name__ == '__main__':
    '''
    For manual testing
    '''
    parser_instance = yacc.yacc()
    s = ''
    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break

        if s == 'sample':
            s = '''int main() {
    return !2;
}
'''

        result = parser_instance.parse(s)

        result.pprint(result)

        print('done with REPL loop')
