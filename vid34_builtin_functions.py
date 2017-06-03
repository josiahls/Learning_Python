"""
Built in functions (functions that dont need to be imported)
"""
import math

x = -1
y = 5

# abs function finds a number's distance from 0
print(abs(x))

if abs(x) == y:
    print('these are the same')
else:
    print('these are not the same')

# help function you can use it to find information
# like a search bar
# you can also leave it blank
#print(help('time'))

# you can use max and min to find
# information about a list
exList = [4,5,4,32,5,56,4,34,4]
print(max(exList))
print(min(exList))

# round function will round a decimal
x = 6.7867665
print(round(x))

# floor and ceil can be used to round directions
print(math.floor(x))
print(math.ceil(x))

# casting:
intMe = '6565'
print(int(intMe))
print(float(intMe))

strMe = 77
print(str(strMe))

