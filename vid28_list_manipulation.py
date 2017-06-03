"""
List Manipulation

"""

# List
x = [5,4,3,5,56,64,45,3,4,6,777,2,2,2,2,2,4,45,32,43,54,76]

# add a value 4 to the end of the list
x.append(4)
print(x)

# insert a number: insert (slot, value)
x.insert(2, 99)
print(x)

# remove (value)
x.remove(2)
print(x)


# slicing data
print(x[3:8]) # inclusive
print(x[-1]) # end of list

# get index
print(x.index(2))

# get count
print(x.count(4))

# sort a list
x.sort()
print(x)

# sorting stringa
y = ['jan', 'jos','bill','alis','joe','bob']
y.sort()
print(y)

