'''
Problem Solving Baekjoon 1934
Author: Injun Son
Date: July 24, 2020
'''
import sys
import math
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(int(A*B/math.gcd(A,B)))
