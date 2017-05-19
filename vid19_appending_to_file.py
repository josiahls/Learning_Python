"""
Goes through explaining how to append text to a file
"""

appendMe = '\n New bit of information'

# do the file .write as an empty call

# opens a stream to append to the existing file
appendFile = open('exampleFile.txt', 'a')
# writes the text to the file
appendFile.write(appendMe)
# closes the stream
appendFile.close()