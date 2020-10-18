'''
Problem Solving Baekjoon 1072
Author: Injun Son
Date: October 18, 2020
'''

from collections import deque
import sys
import math

X, Y = map(int, input().split())
Z = math.floor(100 * Y / X)
low, high = 0, 1000000000
result = 0
#만약 현재 승률이 99라면 절대 100은 될수 없다. 이미 패한 기록이 있기 때문
if Z >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) //2
        tx, ty = X+mid, Y+mid

        if math.floor(100*ty / tx) > Z:
            high = mid -1
            result = mid
        else:
            low = mid +1
    print(result)
