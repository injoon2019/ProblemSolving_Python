'''
Problem Solving Baekjoon 5543
Author: Injun Son
Date: August 4, 2020
'''
from heapq import heappush, heappop
import sys
hamburgers  = [int(input()) for i in range(3)]
drinks = [int(input()) for i in range(2)]
hamburgers.sort()
drinks.sort()
print(hamburgers[0]+drinks[0]-50)