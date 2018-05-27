
#Testing REPL_ENV
i1 = '(+ 1 2)'
r1 = 3

i2 = '(/ (- (+ 5 (* 2 3)) 3) 4)'
r2 = 2

#Testing def!
i3 = '(def! x 3)'
r3 = 3
i4 = 'x'
r4 = 3

i5 = '(def! x 4)'
r5 = 4
i6 = 'x'
r6 = 4

i7 = '(def! y (+ 1 7))'
r7 = 8
i8 = 'y'
r8 = 8

#Verifying symbols are case-sensitive
i9 = '(def! mynum 111)'
r9 = 111
i10 = '(def! MYNUM 222)'
r10 = 222
i11 = 'mynum'
r11 = 111
i12 = 'MYNUM'
r12 = 222

#Check env lookup non-fatal error
i13 = '(abc 1 2 3)'
r13 =  '.*\'abc\' not found.*'
#Check that error aborts def!
i14 = '(def! w 123)'
r14 = 123
i15 = '(def! w (abc))'
r15 = '.*\'abc\' not found.*' #not sure if this is correct, but (abc) should not evaluate to anything
#i16 = 'w' #in scheme this now evaluates to nothing
#r16 = 123

#Testing let*
i17 = '(let* (z 9) z)'
r17 = 9
i18 = '(let* (x 9) x)'
r18 = 9
i19 = 'x'
r19 = 4

i20 = '(let* (z (+ 2 3)) (+ 1 z))'
r20 =  6
i21 = '(let* (p (+ 2 3) q (+ 2 p)) (+ p q))'
r21 = 12
i22 = '(def! y (let* (z 7) z))'
r22 = 7
i23 = 'y'
r23 = 7

#Testing outer environment
i24 = '(def! a 4)'
r24 = 4
i25 = '(let* (q 9) q)'
r25 = 9

i26 = '(let* (q 9) a)'
r26 = 4

i27 = '(let* (z 2) (let* (q 9) a))'
r27 = 4
i28 = '(let* (x 4) (def! a 5))'
r28 = 5
i29 = 'a'
r29 = 4
'''
;>>> deferrable=True
;>>> optional=True
;;
;; -------- Deferrable/Optional Functionality --------

;; Testing let* with vector bindings
(let* [z 9] z)
;=>9
(let* [p (+ 2 3) q (+ 2 p)] (+ p q))
;=>12

;; Testing vector evaluation
(let* (a 5 b 6) [3 4 a [b 7] 8])
;=>[3 4 5 [6 7] 8]
'''

import sys
sys.path.append('../parser')
sys.path.append('../eval')
import lisp_evaluate as eval
import lisp_parser
import lisp_environment


def run_tests():

    print('Running Environment_test.py')

    input_list = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15] + [i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29]
    result_list = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15] + [r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29]


    parser_instance = lisp_parser.get_parser()
    env = lisp_environment.get_environment()

    for (i,k) in (zip(input_list,result_list)):
            
        result = parser_instance.parse(i)
        result = eval.evaluate(result,env)
        print('to be parsed: ' + i)
        print('given: ' + str(result))
        print('expected: '+  str(k))
        assert result == k

    print("Environment_test.py -- Done!")

    return 0


if __name__ == '__main__':
    run_tests()