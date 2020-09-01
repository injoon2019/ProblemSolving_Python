'''
Problem Solving Baekjoon 2110_2
Author: Injun Son
Date: August 13, 2020
'''
import sys
import math

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
dist = houses[-1]-houses[0]

#start end는집 좌표가 아니라 거리
start , end = 1, houses[-1] - houses[0]
answer = 0
def router_counter(dist):
    count = 1
    cur_house = houses[0]
    for i in range(1, N):
        if cur_house+ dist <= houses[i]:
            cur_house = houses[i]
            count +=1

    return count

while start<=end:
    mid = (start+end)//2

    if router_counter(mid)>= C:
        answer = mid
        start = mid+1

    else:
        end = mid -1

print(answer)
