'''
Problem Solving Baekjoon 10974
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(1, N+1)]
used_list = [False]*(N+1)
def back_tacking(cur_count, max_count, used_list, result):
    if cur_count==max_count:
        for i in result:
            print(i, end=" ")
        print()

    else:
        for i in range(1, N+1):
            if used_list[i]==False:
                used_list[i]=True
                back_tacking(cur_count+1, max_count, used_list, result+[i])
                used_list[i]=False

back_tacking(0, N, used_list, [])