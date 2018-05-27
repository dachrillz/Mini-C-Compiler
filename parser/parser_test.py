from c_parser import get_parser

test_string = '''if (a < b) {
    c = 2;
    return c;
} else {
    c = 3;
}'''

test_string = '''int main() {
    return 2;
}
'''

def run_tests():
      
      print("Running parser_test.py")

      parser_instance = get_parser()
      result = parser_instance.parse(test_string)

      print(result)

      print("parser_test.py -- Done!")
      return 0
  

if __name__ == '__main__':
  run_tests()