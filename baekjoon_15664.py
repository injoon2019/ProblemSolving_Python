'''
Problem Solving Baekjoon 15664
Author: Injun Son
Date: September 1, 2020
'''
import sys
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used_list = [False]*N
ans_set = set()
def back_tracking(cur_count, max_count, used_list, result, prev):
    if cur_count == max_count and str(result) not in ans_set:
        ans_set.add(str(result))
        print(' '.join(map(str, result)))
        return

    else:
        for i in range(len(arr)):
            if arr[i] >=prev and used_list[i]==False:
                used_list[i]=True
                back_tracking(cur_count+1, max_count, used_list, result+[arr[i]], arr[i])
                used_list[i] = False

back_tracking(0, M, used_list, [], -1)