'''
Problem Solving Baekjoon 11279
Author: Injun Son
Date: September 7, 2020
'''
import sys
from collections import deque

import heapq
heap = []
heapq._heapify_max(heap)
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    a = int(input())
    if a>0:
        heapq.heappush(heap, (-a, a))
    else:
        if len(heap)>0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

'''
https://www.daleseo.com/python-heapq/
'''