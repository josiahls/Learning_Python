"""
Dictionaries
"""

# generally how you create the dictionary
# the first value is the key, and the second is the value
exDict = {'Jack': 15, 'Bob': 22, 'Alice': 12, 'Kevin': 17}

print(exDict)
# display the value at a certain array
print(exDict['Jack'])

# adding a value to the dictionary
exDict['Tim'] = 14

print(exDict)

# Change a value
exDict['Tim'] = 15

print(exDict)

# remove a value from the dictionary
del exDict['Tim']

print(exDict)

# multi dimensional dictionary
exDict = {'Jack': [15, 'blonde'], 'Bob': [22, 'brown'],
          'Alice': [12, 'gold'], 'Kevin': [17, 'black']}

print(exDict['Jack'])
print(exDict['Jack'][1])

