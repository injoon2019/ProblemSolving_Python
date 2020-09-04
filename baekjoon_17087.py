'''
Problem Solving Baekjoon 17087
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
import copy
import math
import math
N, S = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0]*N
for i in range(len(nums)):
    arr[i] = abs(nums[i]-S)

ans = arr[0]
for i in range(0, N):
    ans = math.gcd(ans, arr[i])

print(ans)