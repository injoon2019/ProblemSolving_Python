'''
Problem Solving Baekjoon 2442
Author: Injun Son
Date: July 15, 2020
'''
import sys
import datetime

N = int(input())
for i in range(1, N+1):
    print(" "*(N-i), end="")
    print("*"* (2*i -1))
    #print(" " * (N - i))
