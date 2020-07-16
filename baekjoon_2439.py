'''
Problem Solving Baekjoon 2439
Author: Injun Son
Date: July 14, 2020
'''
import sys
import datetime

N = int(input())
for i in range(N-1, -1, -1):
    print(' '*i, end='')
    print('*'*(N-i))