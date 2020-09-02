'''
Problem Solving Baekjoon 17298
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(N)]
for i in range(len(nums)):
    try:
        while nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
    except:
        pass
    stack.append(i)

for i in range(len(result)):
    print(result[i], end=" ")
