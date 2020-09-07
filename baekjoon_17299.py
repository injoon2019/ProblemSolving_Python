'''
Problem Solving Baekjoon 17299
Author: Injun Son
Date: September 7, 2020
'''
import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
count_arr = [0]*N
count_dic = dict()
stack = []
ans_arr = [-1]*N

for i in range(N):
    if arr[i] in count_dic:
        count_dic[arr[i]]+=1
    else:
        count_dic[arr[i]]=1

for i in range(N):
    count_arr[i] = count_dic[arr[i]]

for i in range(N):
    ci = count_arr[i]
    while stack and count_arr[stack[-1]] < ci:
        ans_arr[stack.pop()] = arr[i]

    stack.append(i)

print(' '.join(list(map(str, ans_arr))))