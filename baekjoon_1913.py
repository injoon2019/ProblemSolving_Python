'''
Problem Solving Baekjoon 1913
Author: Injun Son
Date: August 26, 2020
'''
import math, sys, copy
# 위 오 아래 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
m = int(input())
snail = []
temp = []
for i in range(n):
    temp.append(0)
for i in range(n):
    snail.append(copy.deepcopy(temp))

move = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
now_x = 0 ; now_y = 0 ; now_num = n*n
while(now_num > 0):
    snail[now_y][now_x] = now_num
    if(now_x + move[d][0] < 0 or now_x + move[d][0] >= n or now_y + move[d][1] < 0 or now_y + move[d][1] >= n or snail[now_y+move[d][1]][now_x+move[d][0]] != 0):
        d = (d + 1) % 4
    now_y = now_y + move[d][1]
    now_x = now_x + move[d][0]
    now_num = now_num - 1

for i in range(n):
    for j in range(n):
        if(snail[i][j] == m):
            find_x = j
            find_y = i
        print(snail[i][j] , end = ' ')
    print()
print(find_y + 1,find_x + 1)

