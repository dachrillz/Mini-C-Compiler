'''
This file handles the code generation for the compiler.
That is it takes the root of the AST and outputs a String that is a legal x86 Assembly program

@TODO:Think about if the 'ifinstance' checks can be implemented more cleanly
'''

import collections
import sys
sys.path.append('../parser')
import c_parser
import c_ast as ast

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
            if isinstance(node, ast.function_node):
                name = node.name
                function_string = '.globl ' + name + '\n' + name + ':'
                stack.appendleft(function_string)

            elif isinstance(node, ast.statement_node):
                if isinstance(node, ast.return_node):
                    value_to_return = stack.popleft()
                    return_string = 'movl' + tab + '$' + str(value_to_return) + ' ,%eax \nret'
                    stack.appendleft(return_string)
                    
                    
            elif isinstance(node, ast.constant_node):
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

        
if __name__ == '__main__':
    
    file_to_compile = sys.stdin.readlines()

    file_to_compile = ''.join(file_to_compile)

    parser_instance = c_parser.get_parser()

    result = parser_instance.parse(file_to_compile)

    result.pprint(result)

    AST_i = AST_visitor()

    AST_i.generate_code(result)