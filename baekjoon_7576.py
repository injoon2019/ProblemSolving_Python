'''
Problem Solving Baekjoon 7576
Author: Injun Son
Date: July 30, 2020
'''
import sys
import copy
sys.setrecursionlimit(100000)

c, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(input().split()) for _ in range(r)]
arr_copy = []
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def spread(y, x):
    for k in range(4):
        ny, nx = y+dy[k], x+dx[k]
        if ny>=0 and ny<r and nx>=0 and nx<c:
            if arr_copy[ny][nx]=='0':
                arr_copy[ny][nx]='1'

count = -1
while arr!= arr_copy:
    count +=1
    arr_copy = copy.deepcopy(arr)
    for i in range(r):
        for j in range(c):
            if arr[i][j]=='1':
                spread(i, j)
    arr, arr_copy = arr_copy, arr


for i in range(r):
    if '0' in arr[i]:
        print(-1)
        exit(0)
else:
    print(count)

'''
시간 초과. 한번 돌때마다 배열을 복사.
차라리 bfs 돌려야할 부분만 queue로 저장
'''