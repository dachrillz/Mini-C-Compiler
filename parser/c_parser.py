import parser.ply.yacc as yacc
from parser.c_ast import *
from parser.lexer import tokens
        
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

    value = t[2]
    if t[1] == '!':
        t[0] = logical_negation_node(value, '!')
    elif t[1] == '-':
        t[0] = negation_node(value, '-')
    elif t[1] == '~':
        t[0] = bitwise_complement_node(value, '~')

def p_exp(t):
    '''exp : unary_op %prec UNARY_OP
           | INTEGER'''

    if type(t[1]) is int:
        t[0] = constant_node(t[1])
    else:
        t[0] = t[1]

def p_statement(t):
    '''statement : RETURN exp SEMICOLON
                  '''
    t[0] = return_node(t[2])

  
def p_error(t):
    import sys
    try:
        print("\tSyntax error at '%s'" % t.value)
        sys.exit() #this is fine for now, but the compiler needs more sophisticated error handling later!
    except AttributeError:
        print("\tSyntax error at '%s'" % t)
        print("custom error!")
        sys.exit()
    parser_instance.errok()


parser_instance = yacc.yacc()

def get_parser():
    return parser_instance


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
    return 2;
}
'''

        result = parser_instance.parse(s)

        result.pprint(result)

        print('done with REPL loop')
