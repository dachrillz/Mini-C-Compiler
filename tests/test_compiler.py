import sys
import os
import glob
import subprocess


path_valid = ['stage_1/valid/', 'stage_2/valid']
path_invalid = ['stage_1/invalid/', 'stage_2/invalid']

if len(sys.argv) == 2:
    path_valid = [sys.argv[1]] 

print('###################################################')
print('############# Testing valid input files! ##########')
print('###################################################')
for item in path_valid:
    print('\t')
    print('\tTesting: ' + item)   
    for filename in glob.glob(os.path.join(item, '*.c')):   

        #call the compiler to generate assembly'
        print('\ttesting file: ' + filename)
        subprocess.call(["python3", '../minic.py', filename]) #@TODO: it feels like this spawns another thread -> check if it is blocking!

        #convert assembly to binary and run it
        child = subprocess.Popen('./run_compiled.sh', shell=True)
        streamdata = child.communicate()[0]
        rc = child.returncode

        if rc is not 0:
            print('\tRecieved error code from executed program! ' + str(rc))

    print()

    


print('###################################################')
print('############# Done testing valid input files! ##########')
print('###################################################')
print()

print('###################################################')
print('############# Testing invalid input files! ##########')
print('###################################################')
for item in path_invalid:
    print('\t')
    print('\tTesting: ' + item)   
    for filename in glob.glob(os.path.join(item, '*.c')):   

        #call the compiler to generate assembly'
        print('\ttesting file: ' + filename)
        subprocess.call(["python3", '../minic.py', filename])
    print()

    #try to run the executable


print('###################################################')
print('############# Done testing invalid input files! ##########')
print('###################################################')

