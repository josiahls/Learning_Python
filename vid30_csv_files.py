"""
Working with CSV files

and 

Error handling
"""

# import module that allows interfacing with CSV files
import csv

# Execute code when importanted
with open('Grocery_Costs_Josiah Sheet.csv') as csvfile:
    # Get list from a csv reader
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    prices = []
    names = []

    # save certain values
    for row in readCSV:
        name = row[0]
        price = row[7]
        prices.append(price)
        names.append(name)

    # go through each row and display it
    for row in readCSV:
        # display a whole row
        print(row)
        # display the first value in the row
        print(row[0])
        print(row[0], row[1])

# display those values
print(prices)
print(names)

# get the index of the price
whatPrice = input('What price are you interested in looking at? ')

try:
    if whatPrice in prices:
        priceIndex = prices.index(whatPrice)

        # get the name of the item with the corresponding index
        theNames = names[priceIndex]

        print('The name of the items with the prices ', whatPrice, ' is ',
              theNames)
    else:
        print("Prioce not found")
# 2.7 is except Exception, e:
# you use Exception or more detailed exceptions
except Exception as e:
    print(e)


