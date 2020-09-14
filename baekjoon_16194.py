'''
Problem Solving Baekjoon 16194
Author: Injun Son
Date: September 14, 2020
'''
from collections import deque
import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = [0]+list(map(int, input().split()))
#dp[i] = 카드 i 개를 갖기 위해 지불해야하는 금액의 최소 값
dp = [sys.maxsize]*(N+1)

for i in range(1, N+1):
    dp[i] = arr[i]

'''
dp[i]를 살 수 있는 경우의 수
j<i 일때 dp[j] 여러번 사기
j<i 일때 dp[j]+dp[n]  (단 j+n ==i)
'''

'''
위에가 잘못된 생각인 이유는
dp[j]+dp[i-j]에 dp[j]여러번 사기가 포함되어있다. dp[j] 여러번 고르는 것이 최소 값이었다면 그 이전에 선택되었을 것이다.

'''

# for i in range(1, N+1):
#     for j in range(1, i):
#         if dp[j] != sys.maxsize:
#             if i%j==0:
#                 dp[i] = min(dp[i], dp[j]*(i//j))
#
#             if dp[i-j] != sys.maxsize:
#                 dp[i] = min(dp[i], dp[j]+dp[i-j])

for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] > dp[i-j]+arr[j]:
            dp[i] = dp[i-j]+arr[j]
print(dp[N])