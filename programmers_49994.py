'''
Problem Solving Programmers 49994
Author: Injun Son
Date: November 19, 2020
'''
import math
from itertools import combinations

# L, D, U, R
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
dirs_dict = {'L':0, 'D':1, 'U':2, 'R':3}

def solution(dirs):
    answer = 0
    path = set()
    y, x = 0, 0
    for move in dirs:
        dir = dirs_dict[move]
        ny, nx = y+dy[dir], x+dx[dir]

        if ny < -5 or ny > 5 or nx < -5 or nx >5:
            continue

        if (y, x, ny, nx) not in path:
            path.add((y, x, ny, nx))
            path.add((ny, nx, y, x))
            answer +=1

        y, x = ny, nx

    return answer

print(solution("ULURRDLLU")) #7
print(solution("LULLLLLLU")) #7
print(solution("LRLRL")) #1

#그래프를 직접 만들지 않고 좌표 값만을 가지고, (기존 위치, 다음위치) 형식으로 path를 set에 저장해야한다는 아이디어는 비교적 쉽게 생각했으나
# 같은 경로를 다른 방향에서 지나칠 때도 같은걸로 처리해야한다는 것을 놓쳤다. 반례가 "LRLRL", 답은 1 이었다.