"""
Module for manipulating OS functions

normally for manipulating directories, however 
useful for many other things
"""

import os
# get the current working directory of the file
curDir = os.getcwd()

print(curDir)

# creates the a new directory
os.mkdir('newDir')

import time
# pause script for 5 seconds
time.sleep(5)

# rename a directory
os.rename('newDir', 'newDir2')

time.sleep(3)
# remove the directory
os.rmdir('newDir2')


