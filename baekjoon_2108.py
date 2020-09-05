'''
Problem Solving Baekjoon 2108
Author: Injun Son
Date: September 5, 2020
'''
from collections import deque
import sys
from itertools import combinations
import math
import math
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
count_arr = [0]*8001
tmp_sum = 0
tmp_max = -1*sys.maxsize
tmp_min = sys.maxsize
for i in range(len(arr)):
    tmp_sum += arr[i]
    count_arr[arr[i]+4000]+=1
    if arr[i] > tmp_max:
        tmp_max = arr[i]
    if arr[i] < tmp_min:
        tmp_min = arr[i]

mode_list = []
for i in range(0, 8001):
    if count_arr[i]!=0:
        mode_list.append([i-4000, count_arr[i]])

mode_list = sorted(mode_list, key = lambda x: (-x[1], x[0]), )
arr.sort()

# print(arr)
# print(mode_list)
'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
print(round(tmp_sum/len(arr)))
print(arr[len(arr)//2])
if len(mode_list)>=2 and mode_list[0][1]==mode_list[1][1]:
    print(mode_list[1][0])
else:
    print(mode_list[0][0])
print(tmp_max - tmp_min)