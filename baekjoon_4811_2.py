'''
Problem Solving Baekjoon 4811_2
Author: Injun Son
Date: September 18, 2020
'''
import sys

#dp[w][h] = 온전한 것 w개, 반쪽짜리 h개일 때 가능한 문자열 개수
dp = [ [0]*32 for _ in range(32)]

#초기화
for h in range(0, 31):
    dp[0][h] = 1

for w in range(1, 31):
    for h in range(31):

        if h==0:
            # 반조각 짜리가 없는 경우, w는 하나 줄고, h는 하나 늘어난 것과 같은 케이스다
            dp[w][h] = dp[w-1][1]
        else:
            #온전한 것도 있고, 반조각 짜리도 있는 경우
            #온전한 것 먹는 경우: w하나 늘고, h하나 늘어난 것과 같은 경우다
            #반쪽 짜리 먹는 경우: 원래 반쪽짜리 있던 것이니, w는 그대로고 h하나 줄어든 것과 같은 경우다
            dp[w][h] = dp[w-1][h+1] + dp[w][h-1]

while True:
    N = int(input())
    if N==0:
        break
    #약통에 반개짜리가 처음에 들어있지 않다
    print(dp[N][0])
