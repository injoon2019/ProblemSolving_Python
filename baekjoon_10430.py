'''
Problem Solving Baekjoon 10430
Author: Injun Son
Date: July 24, 2020
'''
import sys
#A, B, C = map(int, input().split())
A, B, C = map(int, sys.stdin.readline().rstrip().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
