'''
Problem Solving Baekjoon 14890
Author: Injun Son
Date: September 8, 2020
'''
import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
total_count = 0

def checker(num_list):
    global total_count
    # print(num_list)
    rec_list = [[num_list[i],0] for i in range(len(num_list))]
    #rec_list[i] = [i번쨰 숫자, 경사로 설치 유무]
    rec_list[0] = [num_list[0], 0]
    i=1
    for i in range(1, len(num_list)):
        if rec_list[i][1]==1:
            continue

        if num_list[i]== rec_list[i-1][0]:
            rec_list[i] = [num_list[i], 0]

        elif num_list[i] == num_list[i-1]+1:
            for k in range(1, L+1):
                if i-k>=0 and rec_list[i-k][1]==0 and rec_list[i-k][0]==num_list[i]-1:
                    rec_list[i - k][1]= 1
                else:
                    # print("fucked 1", "i", i, k)
                    return

        elif num_list[i] == num_list[i-1]-1:
            for k in range(0, L):
                if i+k <N and rec_list[i+k][1]==0 and rec_list[i+k][0]==num_list[i]:
                    rec_list[i + k][1]=1
                else:
                    # print("fucked 2", "i", i)
                    return

        #높이가 같거나 1차이가 아니면 해결불가능
        else:
            # print("fucked 3", "i", i)
            return
    total_count +=1
    # print("rec_list", rec_list)
    # print(total_count)

def row_func():
    for i in range(N):
        checker(graph[i])

def col_func():
    for j in range(N):
        tmp_list = []
        for i in range(N):
            tmp_list.append(graph[i][j])
        checker(tmp_list)

row_func()
col_func()
print(total_count)