'''
Problem Solving Baekjoon 2156_2
Author: Injun Son
Date: July 17, 2020
'''

n = int(input())
arr =[0]+[int(input()) for _ in range(n)]+[0]
dp = [0]*(n+2)

'''
dp[n]을 n까지의 최대값이라 하자.
그러면 가능한 경우의 수는
1. arr[n]을 안마시기
2. arr[n]을 처음으로 마시기
3. arr[n]을 두번째 잔으로 마시기
'''

dp[1], dp[2] = arr[1], arr[1]+arr[2]

for i in range(3, n+1):
    dp[i] = dp[i-1]  #안마시는 경우
    dp[i] = max(dp[i], dp[i-2]+arr[i])
    dp[i] = max(dp[i], dp[i-3]+arr[i-1]+arr[i])
    '''
    처음에는 세번째 케이스에서 헷갈렸다. dp[i-1}+arr[i]라고하면 안되냐고 생각했기 때문.
    하지만 단순히 dp[i-1]이라고하면 그게 두번째 연속으로 마신건지, 세번째 연속으로 마신건지 알수가 없다
    그래서 확실히 하기위해 dp[i-3]까지 가는 것이다.
    '''

print(dp[n])