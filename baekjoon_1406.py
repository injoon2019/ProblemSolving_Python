'''
Problem Solving Baekjoon 1406
Author: Injun Son
Date: July 24, 2020
'''
import sys
from collections import deque
str = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
deque1 = deque()
deque2 = deque()

for i in range(len(str)):
    deque1.append(str[i])

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'L':
        if len(deque1) > 0:
            deque2.appendleft(deque1.pop())
    elif command[0] == 'D':
        if len(deque2)>0:
            deque1.append(deque2.popleft())
    elif command[0] == 'B':
        if len(deque1)>0:
            deque1.pop()
    elif command[0] == 'P':
        deque1.append(command[1])

for i in deque1:
    print(i, end="")
for i in deque2:
    print(i, end="")