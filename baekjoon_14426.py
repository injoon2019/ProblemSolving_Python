'''
Problem Solving Baekjoon 14426
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
import copy
import math
import math
N, M = map(int, input().split())
list_a = []
count = 0
for _ in range(N):
    s = input()
    list_a.append(s)

for _ in range(M):
    s = input()
    for sentence in list_a:
        if sentence.startswith(s):
            count+=1
            break
print(count)