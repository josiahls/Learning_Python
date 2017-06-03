"""
sys module
"""

import sys

# displays messages usually in red has
# some other small differences also
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
# displays messages in normal color
sys.stdout.write('This is std out text\n')

# this gives the file name, this is useful for
# passing arguements
print(sys.argv)  # example: in cmd do python vid36_sys_module.py 'look at that!'

# if there are more than 1 arguments (more than just the name)
# then display that specific first argument
if (len(sys.argv)) > 1:
    print(sys.argv[1])


# you can also do:
def main(args):
    print(args)


main(sys.argv)
