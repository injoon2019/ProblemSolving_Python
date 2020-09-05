'''
Problem Solving Baekjoon 2293
Author: Injun Son
Date: September 5, 2020
'''
from collections import deque
import sys
n, k = map(int, input().split())
coins =[int(input()) for _ in range(n)]

#dp[j] = j원을 만드는 경우의 수
#dp[j] += dp[j-a[i]] = j원을 만드는 방법 중 하나는 j-a[i]원에서 가치가 a[i]인 동전을 더하면 된다
dp = [0]*(10001)
dp[0]=1
for i in range(n):
    for j in range(coins[i], k+1):
        if j-coins[i]>=0:
            dp[j]+= dp[j-coins[i]]

print(dp[k])

'''
첫 번째 동전만 사용하여 각 k값 마다 가능한 경우의 수를 찾는다.
첫 번째~두 번째 동전만 사용하였을 때, 각k 값 마다 가능한 경우의 수를 찾는다.이 때, 첫 번째 동전만 사용해서 구했던 경우의 수를 활용한다.
첫 번째~n 번째 동전을 사용하였을 때까지 반복한다.
'''