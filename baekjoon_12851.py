'''
Problem Solving Baekjoon 12851
Author: Injun Son
Date: September 15, 2020
'''
from collections import deque
import heapq
import sys, copy

n, k = list(map(int, sys.stdin.readline().split()))

def bfs(n, k):
    #n:시작 지점, k:도착 지점

    #바로 처리할 수 있는 케이스 두 가지
    if n==k:
        return 0, 1
    if n > k:
        return n-k, 1

    #visited[j]는 최소 time
    #ways[j]: j까지 최소로 오는 방법의 수
    q, visited, ways = deque([n]), [sys.maxsize]*100001, [0]*100001
    time, count, success = 0,0, False
    ways[n] = 1
    visited[n] = 0

    while q and not success:
        size = len(q)

        for _ in range(size):
            cur = q.popleft()
            next_move = [cur-1, cur+1, cur*2]
            for j in next_move:
                if j>=0 and j<=100000 and time+1 <=visited[j]:
                    ways[j] +=1
                    visited[j] = time +1

                    if j==k:
                        success = True

                    if not success:
                        q.append(j)
        time +=1

    return visited[k], ways[k]

time, count = bfs(n, k)
print(time)
print(count)