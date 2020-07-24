'''
Problem Solving Baekjoon 10824
Author: Injun Son
Date: July 23, 2020
'''
import sys

arr = list(sys.stdin.readline().rstrip().split())
A = arr[0]+arr[1]
C = arr[2]+arr[3]
print(int(A)+int(C))