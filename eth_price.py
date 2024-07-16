# Script created to create scenarios of different variations of ETH price
# Variation formula is not accurate
# This script is to give you random "possible" ETH prices that change weekly based
# on the price of the week prior. That way you can practice with random scenarios
# to find out if you should buy, sell, how much percentage to look for it, and etc
# Different calculations should be done manually

import random
from tabulate import tabulate

wk =  52
price = int(input("ETH price (INTEGERS ONLY): "))

prices = []
table = []
print()

prices.append(price)

for i in range(wk):

    if i + 1 < wk:
            
        neg_price = price - 500
        pos_price = price + 500 
        price = random.randrange(neg_price, pos_price)

        prices.append(price)


# The table in the making
j = 1
for i in prices:
    table.append([j, i])
    j += 1
        
print(tabulate(table, headers=["Week", "Price (In Dollars)"], tablefmt="pretty"))

