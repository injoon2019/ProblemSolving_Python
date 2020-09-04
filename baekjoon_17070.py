'''
Problem Solving Baekjoon 17070
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys

import sys

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
#dp[i][j][0] = dp[i][j]에 가로로 파이프의 오른쪽 끝이 놓인 경우
#dp[i][j][1] = dp[i][j]에 세로로 파이프의 오른쪽 끝이 놓인 경우
#dp[i][j][2] = dp[i][j]에 대각선으로 파이프의 오른쪽 끝이 놓인 경우
dp = [ [0]*N for _ in range(N)]

def print_board():
    for i in range(N):
        for j in range(N):
            print(dp[i][j], end=" ")
        print("")
    print()

def wall_check(i, j):
    if graph[i][j]!=1 and graph[i-1][j] !=1 and graph[i][j-1]!=1:
        return True
    else:
        return False

#2차원 배열의 원소 하나하나를 길이 3개짜리 list로 초기화
for i in range(N):
    for j in range(N):
        dp[i][j]= [0,0,0]
        
dp[0][1][0]= 1

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            continue
        if j-2>=0: #가로1
            dp[i][j][0]+= dp[i][j-1][0]
        if j-2>=0 and i-1>=0 and wall_check(i,j):
            dp[i][j][2]+= dp[i-1][j-1][0]
        #이전에 세로
        if i-2>=0:
            dp[i][j][1]+=dp[i-1][j][1]
        if j-1>=0 and i-2>=0 and wall_check(i,j):
            dp[i][j][2]+= dp[i-1][j-1][1]
        #이전에 대각선
        if j - 2 >= 0 and i - 1 >= 0:
            dp[i][j][0] += dp[i][j-1][2]
        if j - 1 >= 0 and i - 2 >= 0:
            dp[i][j][1] += dp[i-1][j][2]
        if j - 2 >= 0 and i - 2 >= 0 and wall_check(i,j):
            dp[i][j][2] += dp[i-1][j-1][2]

# print_board()
print(sum(dp[N-1][N-1]))
