'''
Problem Solving Baekjoon 2750
Author: Injun Son
Date: July 22, 2020
'''

N = int(input())
arr = [int(input()) for _ in range(N)]

#삽입 정렬
for i in range(N):
    for j in range(0,i):
        if arr[i]<arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)

