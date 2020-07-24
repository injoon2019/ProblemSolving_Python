'''
Problem Solving Baekjoon 1850
Author: Injun Son
Date: July 24, 2020
'''
import sys
import math
A, B = map(int, input().split())
gcd= math.gcd(A, B)
print("1"*gcd)
