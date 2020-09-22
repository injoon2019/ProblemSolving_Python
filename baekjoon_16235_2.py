'''
Problem Solving Baekjoon 16235_2
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())
#겨울에 더해지는 비료
A = [list(map(int, input().split())) for _ in range(N)]
nutri = [[5 for _ in range(N)] for _ in range(N)]
#tree[i][j][age] = i행 j열에 나이가 age인 나무 개수
tree = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, z = map(int, input().split())
    tree[y-1][x-1][z] = 1

year = 0
while year < K:
    # 봄+여름
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                new_nutri = 0
                tmp = {}
                for age in sorted(tree[i][j].keys()):
                    if age * tree[i][j][age] <= nutri[i][j]:
                        tmp[age+1] = tree[i][j][age]
                        nutri[i][j] -= (age*tree[i][j][age])

                    else:
                        #만약 같은 나이대에 여러 나무가 있는데 모두가 영양분을 먹지는 못하는 상황이면
                        if nutri[i][j] //age:
                            tmp[age+1] = nutri[i][j]//age
                            nutri[i][j] -= (age*tmp[age+1])
                            #살릴 수 있는건 살리고 나머지는 영양분이 된다
                            if tree[i][j][age] - tmp[age+1]:
                                new_nutri += (age//2)*(tree[i][j][age]-tmp[age+1])
                        else:
                            new_nutri += (age//2)*(tree[i][j][age])

                tree[i][j] = tmp
                nutri[i][j] += new_nutri

    #가을
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                num = 0
                for age in tree[i][j].keys():
                    if not (age % 5):
                        num += tree[i][j][age]
                #번식
                if num:
                    for a in range(8):
                        y= i + di[a]
                        x =j + dj[a]
                        if 0<= y<=N-1 and 0<=x<=N-1:
                            if 1 not in tree[y][x]:
                                tree[y][x][1] = num
                            else:
                                tree[y][x][1] += num

    for i in range(N):
        for j in range(N):
            nutri[i][j] += A[i][j]
    year +=1

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += sum(tree[i][j].values())
print(cnt)