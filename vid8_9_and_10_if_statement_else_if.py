"""
If statements
"""

# starting variables
x = 5
y = 8
z = 5

# if statement will not print anything
if x > y:
    print('x is greater than y')

# you can combine boolean operators like this
if z < y > x:
    print('y is greater than z and greater than x')

# you can use <= >= != and ==
if z <= x:
    print('z is less than or equal to x')

"""
If else logic
"""

print('\n\nIf else SECTION')
x = 5
y = 8

# this shows the else being used
if x > y:
    print('x is greater than y')
if x < 55:
    print('x is greater than 55')
else:
    print('x is not greater than y')

"""
elif logic
"""
print('\n\nelif SECTION')
x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
elif 5 > 2:
    print('5 is greater than 2')
else:
    print('if and elif never ran')














