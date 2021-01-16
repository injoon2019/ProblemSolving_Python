'''
Problem Solving Baekjoon 2110_3
Author: Injun Son
Date: January 5, 2021
'''
import sys
import math

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
max_dist = houses[-1] - houses[0]

start, end = 1, max_dist
answer = 0

def router_counter(dist):
    count = 1
    cur_position = houses[0]
    for i in range(1, N):
        if cur_position + dist <= houses[i]: #이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_position = houses[i]

    return count


while start <= end:
    mid = (start + end) // 2

    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)