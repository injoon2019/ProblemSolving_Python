'''
Problem Solving Baekjoon 10972
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(1, N+1)]
used_list = [False]*(N+1)
ans_permu = list(map(int, input().split()))
should_print = False
def back_tacking(cur_count, max_count, used_list, result):
    global should_print
    if cur_count==max_count:
        if should_print:
            for i in result:
                print(i, end=" ")
            exit()
        if result == ans_permu:
            should_print = True


    else:
        for i in range(1, N+1):
            if used_list[i]==False:
                used_list[i]=True
                back_tacking(cur_count+1, max_count, used_list, result+[i])
                used_list[i]=False

back_tacking(0, N, used_list, [])
print(-1)