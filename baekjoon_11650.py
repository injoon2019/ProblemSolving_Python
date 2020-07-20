'''
Problem Solving Baekjoon 11650
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
array = []
for i in range(N):
    x,y = map(int, input().split())
    array.append((x,y))

answer = sorted(array)

for i in answer:
    print(i[0], i[1])