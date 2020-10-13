'''
Problem Solving leetcode best-time-to-buy-and-sell-stock
Author: Injun Son
Date: October 12, 2020
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from typing import *


def maxProfit(prices: List[int]) -> int:
    min_price = sys.maxsize
    max_profit = -sys.maxsize

    for i in prices:
        if i - min_price > max_profit:
            max_profit = i - min_price

        min_price = min(min_price, i)

    return max_profit if max_profit >0 else 0

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
