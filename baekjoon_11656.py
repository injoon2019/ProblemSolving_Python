'''
Problem Solving Baekjoon 10824
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()
lst = []
for i in range(len(str)):
    lst.append(str[i:])

lst.sort()
for i in lst:
    print(i)