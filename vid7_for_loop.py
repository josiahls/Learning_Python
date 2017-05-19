"""
For loops
"""

# list of numbers. this is the python version of arrays however
# arrays.arrays exists to have simpler functionality
exampleList = [1,43,5,6,4,56,4,3,4,6,4566,65,6,5]

# eachNumber is a variable from the list exampleList
# moving from left to right
for eachNumber in exampleList:
    print(eachNumber)

    # this statement is in the for loop
    print('continue program')

# this statement is not in the for loop
print('non-loop program statement')

# this displays all of the numbers in the specified range
# the benifit of range over xrange is instead of creating a list
# for numbers 1 to 11, it generates each value.
# besically saming memory space
for x in range(1,11):
    print(x)

