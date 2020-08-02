'''
Problem Solving Baekjoon 1874
Author: Injun Son
Date: Aug 2, 2020
'''
import sys
import datetime
from collections import deque

N = int(input())
dq = deque([i for i in range(1, N+1)])
result = [int(input()) for i in range(N)]
stack = []
ans = []
i=0
possible = True
print_stack = []
while i <len(result):
    if len(dq) > 0:
        if result[i] > dq[0]:
            print_stack.append("+")
            stack.append(dq.popleft())

        elif result[i] < dq[0]:
            print_stack.append("-")
            ans.append(stack.pop())
            i += 1

        elif result[i]==dq[0]:
            print_stack.append("+")
            stack.append(dq.popleft())
            print_stack.append("-")
            ans.append(stack.pop())
            i += 1

    else:
        if stack[-1] != result[i]:
            possible = False
            break
        else:
            print_stack.append("-")
            ans.append(stack.pop())
            i +=1
if ans != result:
    possible=False

if possible:
    for i in print_stack:
        print(i)
else:
    print("NO")