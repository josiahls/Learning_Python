"""
About tuples and lists.

Tuples are immutable 

Lists are mutable
"""

# Tuple - useful mainly for unpacking data
x = 5, 6, 7, 4, 6
# x = (5, 2, 6, 4, 5) or this

# List - notice the brackets
y = [5, 6, 5, 4, 6]


# Example of a tuple:
def exampleFunc():
    return 15, 6


# If you are concerned about variables being returned in a
# certain order you can use tuples
x, y = exampleFunc()

# Example of another tuple
# we want to show the 1nth element, but they start at 0
x = 5, 6, 7, 4, 6
y = [5, 6, 5, 4, 6]
print(x[1])
print(y[2], y[3])
