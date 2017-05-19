"""
The Shabang line
"""
# This line is used for linux to execute as an executable.
# this is useless line for windows, but it notifies linux about the
# path to python.
# !/usr/bin/python

"""
Explaination of:

if __name__ == '__main__':
"""

def epic():
    print('wow this is great')

if __name__ == '__main__':
    print('such a great module')

# this code is useful if we are going ot call it from another script such as
# import epicthing
# epicthing.epic()
# the if __name__ == '__main__':
# asks if this is the main file being run? or is it being called
# from somewhere else?
