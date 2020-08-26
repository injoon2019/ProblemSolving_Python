'''
Problem Solving Baekjoon 10157
Author: Injun Son
Date: August 26, 2020
'''
import math, sys

c, r = map(int, input().split())
K = int(input())
graph = [[0]*c for _ in range(r)]
count =1

def fill_up(y, x):
    global count
    ret_y, ret_x = 0, 0
    for i in range(y, -1, -1):
        if graph[i][x] !=0:
            ret_y, ret_x = i, x
            print("fillup", ret_y, ret_x)
            break
        else:
            print("fillup", i, x, count)
            graph[i][x]=count
            count +=1
    return ret_y+1, ret_x

def fill_right(y, x):
    x+=1
    global count
    ret_y, ret_x = 0, 0
    for i in range(x, c):
        if graph[y][i] !=0 or i==c-1:
            ret_y, ret_x = y, i
            break
        else:
            graph[y][i]=count
            count +=1
    return ret_y, ret_x

def fill_down(y, x):
    global count
    ret_y, ret_x = 0, 0
    for i in range(y, r):
        if graph[i][x] !=0 or i==r-1:
            ret_y, ret_x = i, x
            print(i, x, count)
            break
        else:
            graph[i][x]=count
            count +=1
    return ret_y, ret_x

def fill_left(y, x):
    global count
    ret_y, ret_x= 0, 0
    for i in range(x, -1, -1):
        if graph[y][i] !=0:
            ret_y, ret_x = y, i
            print("fill left", ret_y, ret_x)
            break
        else:
            graph[y][i]=count
            count +=1
    return ret_y, ret_x

def fill_graph(y, x):
    global count
    ny, nx = fill_up(y, x)
    ny, nx = fill_right(ny, nx)
    ny, nx = fill_down(ny, nx)
    ny, nx = fill_left(ny, nx)
    print("what", ny, nx)
    if 0<=ny-1<r and 0<=nx+1<c and graph[ny-1][nx+1]==0:
        print("check")
        fill_graph(ny-1, nx+1)

fill_graph(r-1, 0)

def print_board():
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end=" ")
        print()

print_board()