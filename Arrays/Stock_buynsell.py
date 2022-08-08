from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    buy = prices[0]
    sell = prices[0]
    profit = sell-buy
    #Greedily going for small buy and rememebering the max profir
    for p in prices:
        if p-buy > profit:
            sell=p
            profit = p-buy
        if p<buy:
            buy=p
    return profit
        
    return sell-buy