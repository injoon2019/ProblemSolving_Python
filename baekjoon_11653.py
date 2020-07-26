'''
Problem Solving Baekjoon 11653
Author: Injun Son
Date: July 26, 2020
'''
import sys
import math

N = int(input())

for i in range(2, 10000001):
    if N==0:
        break
    while(N%i==0):
        print(i)
        N = N//i

