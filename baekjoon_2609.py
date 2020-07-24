'''
Problem Solving Baekjoon 2609
Author: Injun Son
Date: July 24, 2020
'''
import sys
import math
A, B = map(int, input().split())
print(math.gcd(A, B))
print(int(A*B/math.gcd(A,B)))