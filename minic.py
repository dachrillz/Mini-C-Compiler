import sys
#sys.path.append('parser')
#sys.path.append('code_generation/')

import parser.c_parser as c_parser
import code_generation.c_code_generation as c_code_generation

def run_compiler(file_to_compile,out):

    parser_instance = c_parser.get_parser()

    result = parser_instance.parse(file_to_compile)

    AST_i = c_code_generation.get_AST_visitor()

    result = AST_i.generate_code(result)

    write_to = open(out, 'w')
    write_to.write(result)


if __name__ == '__main__':
    
    file_to_compile = open(sys.argv[1], 'r')
    file_to_compile = file_to_compile.readlines()

    file_to_compile = ''.join(file_to_compile)
    

    if len(sys.argv) < 3:
        file_out = 'assembly.s'
    else:
        file_out = open(sys.argv[2])


    run_compiler(file_to_compile,file_out)