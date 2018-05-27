'''
;; Testing evaluation of arithmetic operations

;; -------- Deferrable/Optional Functionality --------

;; Testing evaluation within collection literals
[1 2 (+ 1 2)]
;=>[1 2 3]

{"a" (+ 7 8)}
;=>{"a" 15}

{:a (+ 7 8)}
;=>{:a 15}

'''
import sys
sys.path.append('../parser')
import lisp_evaluate as eval
import lisp_parser


def run_tests():
    
    
    print("Running eval_test.py")

    def simple_addition(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = 0
        for item in arg:
            result += item
        return result


    def simple_subtraction(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = arg[0]
        for i in range(1, len(arg)):
            result -= arg[i]
        return result


    
    def simple_multiplication(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = 1
        for item in arg:
            result *= item
        return result


    
    def simple_division(arg):
        '''
        @TODO: think about rewriting this using function closures instead
        '''
        result = arg[0]
        for i in range(1, len(arg)):
            result /= arg[i]
        return result


    env = {'+' : simple_addition, '-': simple_subtraction, '*': simple_multiplication,'/': simple_division}

    parser_instance = lisp_parser.get_parser()

    result = parser_instance.parse("1")
    result = eval.evaluate(result,env)
    assert result == 1

    result = parser_instance.parse("(+ 5 (* 2 3))")
    result = eval.evaluate(result,env)
    assert result == 11

    result = parser_instance.parse("(- (+ 5 (* 2 3)) 3)")
    result = eval.evaluate(result,env)
    assert result == 8

    result = parser_instance.parse("(/ (- (+ 5 (* 2 3)) 3) 4)")
    result = eval.evaluate(result,env)
    assert result == 2

    result = parser_instance.parse("(/ (- (+ 515 (* 87 311)) 302) 27)")
    result = eval.evaluate(result,env)
    assert result == 1010

    result = parser_instance.parse("(* -3 6)")
    result = eval.evaluate(result,env)
    assert result == -18

    result = parser_instance.parse("(/ (- (+ 515 (* -87 311)) 296) 27)")
    result = eval.evaluate(result,env)
    assert result == -994

    result = parser_instance.parse("(abc 1 2 3)")
    result = eval.evaluate(result,env)
    assert result == ".*\'abc\' not found.*" #Need to write some error handling here

    result = parser_instance.parse("()")
    result = eval.evaluate(result,env)
    assert result == '()'#Should this be some special kind of data?

    result = parser_instance.parse("(+ 1 2)")
    result = eval.evaluate(result,env)
    assert result == 3

    print("Eval_test.py -- Done!")

    return 0



if __name__ == '__main__':
    run_tests()