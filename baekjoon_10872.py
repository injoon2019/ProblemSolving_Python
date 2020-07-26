'''
Problem Solving Baekjoon 10872
Author: Injun Son
Date: July 26, 2020
'''
import sys
import math

N = int(input())

def Factorial(N):
    if N==0:
        return 1

    return N*Factorial(N-1)

print(Factorial(N))