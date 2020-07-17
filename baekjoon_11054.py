'''
Problem Solving Baekjoon 11054
Author: Injun Son
Date: July 17, 2020
'''
import copy

N = int(input())
arr = list(map(int, input().split()))
dp_dec = [1]*N
dp_inc = [1]*N
#dp[i] = i를 선택하고,i까지 합이 가장 큰 증가 부분 수열의 합
for i in range(N-1,-1, -1):
    for j in range(N-1,i, -1):
        if arr[i] > arr[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)

for i in range(1,N):
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)

ans = [0]*N
for i in range(N):
    ans[i] = dp_dec[i]+dp_inc[i]


print(max(ans)-1)

'''
처음 생각: 증가수열과 감소수열을 구해서 합이 가장 큰걸 고르면되지않을까? 
 -> 어디까지 증가했다가 감소했는지가 전혀 기록되지 않으므로 일관성이 없다.
 답: 왼쪾에서 오른쪽으로 증가, 오른쪽에서 왼쪽으로 증가 이 방식으로 구한다. 
'''