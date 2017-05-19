"""
Statistics
"""
# module for performing statistics functions
#import statistics
import statistics as s

# or we can import function directly by:
# from statistics import variance as v, mean
# then we could have lines such as
# x = v(exampleList)
# x = mean(exampleList)

# can also do: from statistics import *
# to call functions directly from the whole file

# create a list of values
exampleList = [3, 4, 45, 4, 65, 5, 34, 56, 6, 5, 5, 4, 4]

# calls the mean function of the statistics module
# x = statistics.mean(exampleList) since we are referencing statistics as 's'
# we can just do this:
x = s.mean(exampleList)

print(x)

# calculate and display the variance
x = s.variance(exampleList)
print(x)

