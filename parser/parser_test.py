from lisp_parser import get_parser

test_list = ['1',
'7',
'  7',   
'-123',
'+',
'abc',
'   abc',   
'abc5',
'abc-def',
'(+ 1 2)',
'()',
'(nil)',
'((3 4))',
'(+ 1 (+ 2 3))',
'  ( +   1   (+   2 3   )   )',  
'(* 1 2)',
'(** 1 2)',
'(* -3 6)']
#'(1 2, 3,,,,),,'] #currentyl produces error

def run_tests():
      
      print("Running parser_test.py")

      parser_instance = get_parser()

      for item in test_list:
            result = parser_instance.parse(item)

            assert result is not None
            assert 'Syntax error' not in result

      print("parser_test.py -- Done!")
      return 0
  

if __name__ == '__main__':
  run_tests()