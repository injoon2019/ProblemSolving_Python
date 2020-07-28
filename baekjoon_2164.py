'''
Problem Solving Baekjoon 2164
Author: Injun Son
Date: July 28, 2020
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [i for i in range(1, N+1)]
queue = deque(arr)
while queue:
    if len(queue)==1:
        print(queue.pop())
        break;
    queue.popleft()
    queue.append(queue.popleft())

