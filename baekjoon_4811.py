'''
Problem Solving Baekjoon 4811
Author: Injun Son
Date: September 18, 2020
'''
import sys

#dp[w][h]= 온전한 알약이 w개 반쪽짜리 알약이 h개 있을 때
#만들 수 있는 문자열의 개수
dp = [[0]*32 for _ in range(32)]

for i in range(31):
    #초기화
    #온전한 알약이 0개이면, 만들수 있는 문자열의 개수는 1개이다
    dp[0][i] = 1

for w in range(1, 31):
    for h in range(0, 31):
        if h==0:
            #쪼개진 알약이 없는 경우 
            dp[w][h] = dp[w-1][1]
        else:
            #온전/쪼개진 알약 모두가 있는 경우
            dp[w][h] = dp[w-1][h+1] + dp[w][h-1]

while True:
    N = int(input())
    if N==0:
        break

    #온전한 약들만 들어서 시작하기 때문에 무조건 처음은 쪼개 먹는다
    #따라서 dp[N-1][1]의 값을 찾으면 된다
    print(dp[N-1][1])

