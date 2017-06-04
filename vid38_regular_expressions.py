"""
Regular expressions: SUPER IMPORTANT

identifiers:
\ notification that something is a character
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
/W anything but a character
. any character, except a new line
\b the white space around words
\. a period

Modifiers (hey we are looking  this amount, type, ect..):
{1,3} we're expecting 1-3 ex: \d{1-3}
+ match 1 or more 
? match 0 or 1
* match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or ex: \d{1-3} | \w{5-6}
[] range or "variance" ex: {A-Za-z} or {A-Z} or {1-5a-qA-z}(this means any of the following)
{x} expecting "x' amount

White Space Characters (characters you dont see):
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET:
. + * ? [ ] $ ^ ( ) { } | \
"""

import re

exampleString = '''
Jessica is 15 years old, and danial is 27 years old. 
Edward is 97, and his grandfather, Oscar , is 102.
'''

# specify the regular expressions that coorespond to names
# findall((the r indicates it is a regular expression)the regex,
# and the string to search)
# there are other reguylar expression function functions
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

# create a dictionary
ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)

