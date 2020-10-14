'''
Problem Solving Baekjoon 1018_2
Author: Injun Son
Date: October 14, 2020
'''

from collections import deque
import sys

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
min_ans = sys.maxsize

def count_change(y, x):
    black_start = 0
    white_start = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if (i+j) %2 ==0:
                #짝수칸이면 W여야한다는 가정
                if graph[i][j] != 'W':
                    white_start +=1
                #짝수칸이면 B여야한다는 가정
                if graph[i][j] != 'B':
                    black_start +=1
            else:
                #홀수칸이면 B여야한다는 가정 == 짝수칸이면 W여야한다는 가정
                if graph[i][j] != 'B':
                    white_start +=1
                #홀수칸이면 W여야한다는 가정
                if graph[i][j] != 'W':
                    black_start +=1

    return min(black_start, white_start)

for i in range(0, N-8+1):
    for j in range(0, M-8+1):
        min_ans = min(min_ans, count_change(i, j))

print(min_ans)