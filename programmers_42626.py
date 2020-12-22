'''
Problem Solving Programmers 42626
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)

    while len(heap) >= 2:
        if heap[0] >= K or len(heap) < 2:
            break
        min_hot = heapq.heappop(heap)
        min_next_hot = heapq.heappop(heap)
        heapq.heappush(heap, min_hot + min_next_hot * 2)
        answer +=1

    if heap[0] < K:
        return -1
    else:
        return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1, 1], 5))
# print(solution([1, 1], 1))
print(solution([1, 1, 1], 4), 2)