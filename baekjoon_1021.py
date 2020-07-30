'''
Problem Solving Baekjoon 1021
Author: Injun Son
Date: July 30, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

def move_left(target):
    count = 0
    while deq1[0] != target:
        deq1.append(deq1.popleft())
        count +=1
    if deq1[0]==target:
        deq1.popleft()
    return count

def move_right(target):
    count = 0
    while deq2[0] != target:
        deq2.appendleft(deq2.pop())
        count +=1
    if deq2[0]==target:
        deq2.popleft()
    return count

N, M = map(int, sys.stdin.readline().rstrip().split())
remove = list(map(int, sys.stdin.readline().rstrip().split()))
deq1 = deque([i for i in range(1, N+1)])
deq2 = deque([i for i in range(1, N+1)])

ans = 0
for i in remove:
    ans += min(move_left(i), move_right(i))

print(ans)