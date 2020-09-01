'''
Problem Solving Baekjoon 11729_2
Author: Injun Son
Date: September 1, 2020
'''
import sys
from collections import deque

N = int(input())
move_count = 0
ans_list = []
def move(start, end):
    global move_count
    move_count +=1
    ans_list.append([start, end])

def Hannoi(n, start, by, end):
    if n==1:
        move(start, end)
        return
    else:
        Hannoi(n-1, start, end, by)
        move(start, end)
        Hannoi(n - 1, by, start, end)


Hannoi(N, 1, 2 ,3)
print(move_count)
for i in ans_list:
    print(i[0], i[1])
'''
N개의 원판이 있고, start, by, end가 있다면
N-1개의 원판을 by에 옮기는 것이 우선이다
그다음 맨 밑의 원판을 end로 옮긴다
그리고 N-2개의 원판을 옮기고
N-2번쨰 원판을 end로 옮긴다
'''