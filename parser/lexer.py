import ply.lex as lex


#Define tokens
tokens = [
   'NUMBER',
   'LPAREN',
   'RPAREN',
    'SYMBOL'
]


reserved = {
}


tokens += reserved.values()

#specify the tokens
#separators
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'[-]?\d+' 
    try:
        t.value = int(t.value) 
    except ValueError:
        print("Integer value too large %d", t.value) #handle overflow here
        t.value = 0 
    return t

def t_SYMBOL(t):
    r'[^0-9()][^()\ \t\n]*'
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
    
    sample_program = """
    class Factorial {
        public static void main(String[] a){
            System.out.println(new Fac().ComputeFac(10));
        }
    }

    class Fac {
        public int ComputeFac(int num){
            in num_aux;
            if (num < 1)
                num_aux = 1;
            else
                num_aux = num * (this.ComputeFac(num-1));
            return num_aux;
        }
    }
    """


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
