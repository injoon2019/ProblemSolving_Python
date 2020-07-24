'''
Problem Solving Baekjoon 1168
Author: Injun Son
Date: July 24, 2020
'''
N, K = map(int, input().split())
queue = [i for i in range(1, N+1)]

index = 0
arr = []
while queue:
    index = (index+K-1) % len(queue)
    arr.append(str(queue.pop(index)))

print("<", ", ".join(arr), ">", sep="")