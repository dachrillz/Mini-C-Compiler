import ply.lex as lex

'''
Tokens for minimal C

    Open brace {
    Close brace }
    Open parenthesis \(
    Close parenthesis \)
    Semicolon ;
    Int keyword int
    Return keyword return
    Identifier [a-zA-Z]\w*
    Integer

'''

#Define tokens
tokens = [
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'IDENTIFIER',
    'INTEGER'
]


reserved = {
    'int' : 'INT',
    'return' : 'RETURN'
}


tokens += list(reserved.values())

#specify the tokens
#separators
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'

def t_INTEGER(t):
    r'[-]?\d+' 
    try:
        t.value = int(t.value) 
    except ValueError:
        print("Integer value too large %d", t.value) #handle overflow here
        t.value = 0 
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z]\w*'
    t.type = reserved.get(t.value,'IDENTIFIER') #check for reserved words!
    return t

#ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


lexer_instance = lex.lex()


if __name__ == '__main__':
    
    sample_program = '''int main() {
    return 2;
}
'''


    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break
        if s == 'sample':
            s = sample_program
        lexer_instance.input(s) #feed data to the lexer
        while True:
            current_token = lexer_instance.token() #get next token in queue

            if not current_token:
                break   
            print(current_token)
