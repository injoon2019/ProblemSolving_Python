'''
Problem Solving Baekjoon 2110
Author: Injun Son
Date: August 9, 2020
'''
import sys
import math
def router_counter(distance):
    count =1
    cur_house = arr[0] #시작점
    for i in range(1, N): #집모두를 돈다
        if cur_house + distance <= arr[i]: #이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count +=1
            cur_house = arr[i] #공유기 설치된 집 갱신
    return count

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
#start end 는 집 좌표가 아닌 거리
start , end = 1, arr[-1]-arr[0] #이분 탐색해야할 거리

while start <= end:
    mid = (start+end)//2

    if router_counter(mid)>=C:
        answer = mid
        start = mid +1
    else:
        end = mid -1

print(answer)