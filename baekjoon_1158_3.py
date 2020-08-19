'''
Problem Solving Baekjoon 1158_3
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
ans_nums = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    ans_nums.append(str(q.popleft()))


print('<', ", ".join(ans_nums), ">", sep="")