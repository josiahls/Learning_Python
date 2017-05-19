"""
Talking about while loops
"""

# condition that the loop follows
condition = 1

# loop says loop while condition less than 10
while condition < 10:
    # display the condition
    print(condition)
    # increments condition: condition = condition + 1
    condition += 1

# you can have a inf loop using values True or False
while True:
    print('doing stuff')
