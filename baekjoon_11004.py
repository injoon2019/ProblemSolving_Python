'''
Problem Solving Baekjoon 11004
Author: Injun Son
Date: July 23, 2020
'''
import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print(arr[K-1])
