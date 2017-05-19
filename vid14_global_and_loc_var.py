"""
Global and Local variables

Global is a variable that can be accessed anywhere

Local can be accessed in one location


"""

x = 6


def example():
    # this states the x is a global not a local variable
    # global x you can do this but it is frowned upon
    # you can receive the value of x such as globx = x
    globx = x
    print(globx)
    print(globx + 6)
    globx += 5

    return globx


x = example()
print(x)
