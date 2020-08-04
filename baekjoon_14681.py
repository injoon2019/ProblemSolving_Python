'''
Problem Solving Baekjoon 14681
Author: Injun Son
Date: August 4, 2020
'''
from heapq import heappush, heappop
import sys
arr = [int(input()) for i in range(2)]
if arr[0]>0 and arr[1]>0:
    print(1)
elif arr[0]<0 and arr[1]>0:
    print(2)
elif arr[0]<0 and arr[1]<0:
    print(3)
else:
    print(4)