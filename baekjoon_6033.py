'''
Problem Solving Baekjoon 5014
Author: Injun Son
Date: August 20, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
def back_tracking(cur_count, max_count, result, used_list, prev):
    global ans
    if cur_count == max_count:
        ans.append(result)
    for i in range(0, len(arr)):
        if used_list[arr[i]]==False and arr[i]>prev:
            used_list[arr[i]]=True
            back_tracking(cur_count+1, max_count, result+[arr[i]], used_list, arr[i])
            used_list[arr[i]]=False

while True:
    arr = list(map(int, input().split()))
    if arr[0]!=0:
        arr = arr[1:]
        ans = []
        used_list = [False]*50
        back_tracking(0, 6, [], used_list, -1)
        for ans_list in ans:
            for k in ans_list:
                print(k, end=" ")
            print("")
        print("")
    else:
        exit()
