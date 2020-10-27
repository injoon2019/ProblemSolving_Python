'''
Problem Solving Baekjoon 1347
Author: Injun Son
Date: October 26, 2020
'''
import sys
import math

'''
순차적인 아이디어:
1. 큰 2차원 배열을 만들고 직접 이동하는 것들을 시뮬레이션하면되지 않을까
2. 그 2차원 배열을 미리 '#', 즉 벽으로 채워놓으면 되지 않을까 
3. 그런데 큰 2차원 배열에서 정답에 해당하는 부분만 어떻게 찾아내지? -> 발상 못함
4. 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다고 했으니,
제일 왼쪽 행, 제일 위 열, 제일 오른쪽 행, 제일 아래쪽 열을 구하면된다! 
'''
#방향: 남 서 북 동
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
graph = [ ['#']*111 for _ in range(111)]
dir = 0
N = int(input())
command_list = input()
cur_y, cur_x = 50, 50
graph[cur_y][cur_x]='.'

leftmost_x, rightmost_x = 111, -1
highest_y, lowest_y = 111,-1

for command in command_list:
    if command == 'R':
        dir = (dir+1)%4

    elif command == 'L':
        if dir >=1:
            dir -=1
        elif dir==0:
            dir = 3
    else:
        cur_y += dy[dir]
        cur_x += dx[dir]
        graph[cur_y][cur_x] = '.'

for i in range(111):
    for j in range(111):
        if graph[i][j]=='.':
            if j < leftmost_x:
                leftmost_x = j

            if i < highest_y:
                highest_y = i

            if j > rightmost_x:
                rightmost_x = j

            if i > lowest_y:
                lowest_y = i


for i in range(highest_y, lowest_y+1):
    for j in range(leftmost_x, rightmost_x +1):
        print(graph[i][j], end="")
    print()