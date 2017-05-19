"""
Function parameter default values
"""

# the keyword pass gives it something to do
# so you do not get an error
def simple(num1, num2):
    pass

# this sets the default parameter
def simple(num1, num2=5):
    print(num1, num2)

# sample function using default values
def basic_window(width, height, font='TNR', bgc='w', scrollbar=True):
    print(width, height, font, bgc)

# this makes use of default values
basic_window(500, 350)

# you can skip setting certain defaults by naming the parameter
basic_window(4500, 350, bgc='b')