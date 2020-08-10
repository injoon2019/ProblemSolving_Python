'''
Problem Solving Baekjoon 1780
Author: Injun Son
Date: August 10, 2020
'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [0,0,0] #-1, 0, 1

def is_allSame(start_y, start_x, size):
    start_num = graph[start_y][start_x]
    allSame = True
    for i in range(start_y, start_y+size):
        for j in range(start_x, start_x+size):
            if graph[i][j] != start_num:
                allSame=False
                for a in range(3):
                    for b in range(3):
                        is_allSame( (start_y)+(size//3)*a, (start_x)+(size//3)*b, size//3)
                return

    if allSame:
        result[start_num]+=1
    return

is_allSame(0,0,N)
for i in range(-1, len(result)-1):
    print(result[i])
