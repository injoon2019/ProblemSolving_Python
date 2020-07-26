'''
Problem Solving Baekjoon 1676
Author: Injun Son
Date: July 26, 2020
'''
import sys
import math

N = int(input())

count = 0
count += N//5
count += N//25
count += N//125
print(count)