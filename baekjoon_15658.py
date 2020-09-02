'''
Problem Solving Baekjoon 15658
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
mx, mn = -1*sys.maxsize, sys.maxsize

def solve(index, ans, add, sub, mul, div):
    global mx, mn
    if index >= N:
        mx = max(mx, ans)
        mn = min(mn, ans)
        return
    if add:
        solve(index+1, ans+nums[index], add-1, sub, mul, div)
    if sub:
        solve(index+1, ans-nums[index], add, sub-1, mul, div)
    if mul:
        solve(index+1, ans*nums[index], add, sub, mul-1, div)
    if div:
        solve(index+1, ans//nums[index] if ans >0 else -((-ans)//nums[index]), add, sub, mul, div-1)

solve(1, nums[0], operators[0], operators[1], operators[2], operators[3])
print(mx)
print(mn)