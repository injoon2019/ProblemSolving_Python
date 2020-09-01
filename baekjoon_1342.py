'''
Problem Solving Baekjoon 1342
Author: Injun Son
Date: August 31, 2020
'''
import sys
import math

ans =0
ans_list = dict()
def back_traacking(cur_count, max_count, used_list, string, prev):
    global ans, ans_list
    if cur_count == max_count and string not in ans_list:
        ans +=1
        ans_list[string]=1
    else:
        for i in range(0, len(S)):
            if used_list[i]==False and S[i] != prev:
                used_list[i]=True
                back_traacking(cur_count+1, max_count, used_list, string+S[i], S[i])
                used_list[i] = False
S = input()
used_list = [False]*len(S)
back_traacking(0, len(S), used_list, '', '')

print(ans)