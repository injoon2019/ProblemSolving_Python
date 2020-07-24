'''
Problem Solving Baekjoon 1158
Author: Injun Son
Date: July 24, 2020
'''
from collections import deque
N, K = map(int, input().split())
dq = deque()
for i in range(N):
    dq.append(i+1)
removed = []
while len(dq)>0:
    for _ in range(K-1):
        dq.append(dq.popleft())
    removed.append(dq.popleft())

print("<", end="")
for i in range(len(removed) -1):
    print(str(removed[i])+", ", end="")
print(str(removed[-1])+">")