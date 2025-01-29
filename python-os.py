# finding current working directory
import os
def getcws():
    a=os.getcwd()
    print(a)
getcws()
os.chdir('../')
getcws()