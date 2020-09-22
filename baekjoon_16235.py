'''
Problem Solving Baekjoon 16235
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

#N*N 땅, M 나무 개수, K년이 지난 후
N, M, K = map(int, input().split())
#graph에는 영양분의 상태가 저장되어있다. 초기에는 전부 5다
graph = [ [5]*N for _ in range(N)]
#trees[i][j]에는 (i,j)칸에 있는 나무들의 나이들이 리스트로 들어있다
trees = [[None]*N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        trees[i][j] = deque()

add_graph = []
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

for _ in range(N):
    tmp = list(map(int, input().split()))
    add_graph.append(tmp)

for _ in range(M):
    y, x, k = map(int, input().split())
    x-=1; y-=1
    #나이와 살아있음 유무 정보를 저장
    trees[y][x].append([k, 1])

def spring_function():
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree[0] !=0:
                    if graph[i][j] >= tree[0]: #tree의 나이 이상으로 영양분이 있다면
                        graph[i][j] -= tree[0] #tree의 나이만큼 영야분을 먹고
                        tree[0] += 1 #tree는 나이를 1살 먹는다
                    else:
                        tree[1] = 0 #만약 양분을 못먹으면 죽는다

def summer_function():
    for i in range(N):
        for j in range(N):
            remove_index= []
            for k in range(len(trees[i][j])):
                if trees[i][j][k][1]==0: #만약 죽은 나무라면
                    graph[i][j] += (trees[i][j][k][0]//2)
                    remove_index.append(k)
                    trees[i][j][k] = [0,0]


#번식
def fall_function():
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree[0] %5 ==0 and tree[0]!=0:
                    for dir in range(8):
                        ny, nx = i+dy[dir], j+dx[dir]
                        if ny<0 or ny>=N or nx<0 or nx>=N:
                            continue
                        trees[ny][nx].append([1, 1]) #나이가 한살이고 살아있는 나무를 근처에 추가


def winter_function():
    for i in range(N):
        for j in range(N):
            graph[i][j] += add_graph[i][j]

def year_function():
    spring_function()
    summer_function()
    fall_function()
    # print_board(trees)
    # print("after breed")
    winter_function()

for _ in range(K):
    year_function()

alive_tree = 0
for i in range(N):
    for j in range(N):
        for tree in trees[i][j]:
            if tree[0] != 0:
                alive_tree += 1

# print_board(trees)
print(alive_tree)

'''
시간 초과가 났다
'''