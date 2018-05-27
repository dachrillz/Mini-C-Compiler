import sys
sys.path.append('parser')
sys.path.append('eval')
sys.path.append('environment')
#import mymodule

import parser_test
import eval_test
import environment_test


print(parser_test.run_tests())
print(eval_test.run_tests())
print(environment_test.run_tests())