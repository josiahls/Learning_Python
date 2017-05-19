"""
Goes through explaining how to read from a file
"""

# reads the entire file
readMe = open('exampleFile.txt','r').read()
print(readMe)

print('\n\nLine by line reading')

readMe = open('exampleFile.txt','r').readlines()
print(readMe)