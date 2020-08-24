'''
Problem Solving Baekjoon 1002
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
import math

sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    #두 원의 중심 사이의 거리
    d=  math.sqrt((x1-x2)**2 + (y1-y2)**2)
    R= [r1, r2, d]
    m = max(R)
    R.remove(m)

    # 두 원이 일치하는 경우
    if (d==0 and r1==r2):
        print(-1)

    # 두 원이 한 점에서 만나는 경우
    elif (d==r1+r2) or (m==sum(R)):
        print(1)

    #만나지 않는 경우
    elif m> sum(R):
        print(0)

    else:
        print(2)