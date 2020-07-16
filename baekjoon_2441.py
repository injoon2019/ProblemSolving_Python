'''
Problem Solving Baekjoon 2441
Author: Injun Son
Date: July 15, 2020
'''
import sys
import datetime

N = int(input())
for i in range(N, -1, -1):
    print(" "*(N-i), end="")
    print("*"*i)