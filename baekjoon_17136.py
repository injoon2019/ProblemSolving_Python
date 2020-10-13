'''
Problem Solving Baekjoon 17136
Author: Injun Son
Date: October 13, 2020
'''

from collections import deque
import sys

def print_board():
    global graph
    for i in range(10):
        for j in range(10):
            print(graph[i][j], end=" ")
        print()
    print()

def check_cover(y, x, n):
    global graph
    for i in range(y, y+n):
        for j in range(x, x+n):

            if i>=10 or j>=10 or graph[i][j]==0:
                return False
    return True

def change_zero(y, x, n):
    global graph
    for i in range(y, y+n):
        for j in range(x, x+n):
            graph[i][j] = 0

def change_one(y, x, n):
    global graph
    for i in range(y, y+n):
        for j in range(x, x+n):
            graph[i][j] = 1

def get_sum():
    global graph
    tmp_sum = 0
    for i in range(len(graph)):
        tmp_sum += sum(graph[i])

    return tmp_sum

graph = [list(map(int, input().split())) for _ in range(10)]
pos_list = []
paper_list = [5, 5, 5, 5, 5]
min_count = sys.maxsize

def back_tracking(paper_left, count):
    global min_count, graph
    if count >= min_count:
        return

    if get_sum()==0:
        min_count = min(min_count, count)
        return

    for y in range(10):
        for x in range(10):
            if graph[y][x] ==1:
                # print_board()
                for i in range(len(paper_left)-1, -1, -1):
                    # print_board()
                    if paper_left[i] > 0 and check_cover(y, x, i+1):
                        # print_board()
                        paper_left[i] -=1
                        change_zero(y, x, i+1)
                        # print_board()
                        back_tracking(paper_left, count+1)
                        change_one(y, x, i + 1)
                        paper_left[i] +=1

                    elif paper_left[i] <=0:
                        return

back_tracking(paper_list, 0)

print(-1 if min_count==sys.maxsize else min_count)