'''
Problem Solving Baekjoon 2869
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

A, B, V = map(int, sys.stdin.readline().rstrip().split())
if A>=V:
    print(1)
else:
    if (V-A)%(A-B) ==0:
        print( (V-A)//(A-B) +1)
    else:
         print( (V-A)//(A-B) +2)