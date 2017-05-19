"""
Function parameters
"""

# this is how variables are passed
# very similar to java
def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is ', num1)
    print(answer)

# this call relys on variable order
simple_addition(5, 3)

# or rarely you can do this
simple_addition(num2=4, num1=2)