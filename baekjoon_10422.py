'''
Problem Solving Baekjoon 10422
Author: Injun Son
Date: September 18, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
MOD = 1000000007
t = int(input())
lst = []
'''
https://naivep.tistory.com/75
올바른 괄호를 만들기 위해서 
길이가 i 라고 하자
(****)******
두 번째 괄호를 j 번째라고하면
괄호 안에 공간의 개수는 j-2이고, 오른쪽은 i-j이다
dp[i] = dp[j-2]*dp[i-j] (2<= j<=i)이다 
'''

for _ in range(t):
    lst.append(int(input()))

dp = [0]* 5001
dp[0] = 1

for i in range(2, 5001, 2):
    for j in range(2, i+1, 2):
        dp[i] += (dp[j-2] * dp[i-j]) % MOD

for i in lst:
    print(dp[i] % MOD)