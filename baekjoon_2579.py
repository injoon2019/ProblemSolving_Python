'''
Problem Solving Baekjoon 2579
Author: Injun Son
Date: July 17, 2020
'''
import copy

N = int(input())
arr = [int(input()) for _ in range(N)]
#마지막 계단을 꼭 밟아야하니, 배열을 뒤집어서 마지막 것을 밟고 역행한다.
arr.reverse()
arr = [0] + arr+[0]*2
dp = [0]*(N+3)
'''
dp[i]를 i까지의 최대값이라하면, 
1. 직전것을 밟는 경우 dp[i-3]+arr[i-1]+arr[i]
2. 직전 것을 안밟는경우 dp[i-2] + arr[i]
'''
dp[1] = arr[1]
dp[2] = arr[1]+arr[2]
dp[3] = arr[1]+arr[3]
for i in range(4, N+1):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

'''
처음했을 때는 dp[2]까지만 정의했다. 그러면 반례
6 100 1 1 100 1  
에서 정답이 202인데 207을 반환한다. 마지막 것을 밟지 않기 때문이다.
그래서 처음 dp[3]의 경우 애초에 중간에 것을 안밟게해야한다. 
'''
print(max(dp))