"""
Writing to the file

there are to ways to write to a file:

Writing: erasing file, and than writing new text to it
Appending: adding text to existing text in file
"""

text = 'Sample text to Save\nNew Line';

# create an object for writing to a file. 'w' means we are in write mode
saveFile = open('exampleFile.txt', 'w')

# you can also specify a file path
# open('../exampleFile.txt')

# writing the text to the file
saveFile.write(text)

# close the stream
saveFile.close()



