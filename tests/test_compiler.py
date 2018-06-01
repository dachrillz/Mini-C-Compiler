import sys
from subprocess import call


#call the compiler to generate assembly
current_file = '../trivial.c'
call(["python3", '../minic.py' ,current_file])

#try to run the executable
