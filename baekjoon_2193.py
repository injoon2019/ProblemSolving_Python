'''
Problem Solving Baekjoon 2193
Author: Injun Son
Date: July 16, 2020
'''

N = int(input())

arr = [[0 for c in range(0,2)] for r in range(0,90+1)]
#arr[i][j] = 길이가 i이고 j로 끝나는 수의 개수

arr[1][1] = 1
arr[2][0] = 1

for r in range(3, N+1):
    arr[r][0] = arr[r-1][0]+arr[r-1][1]
    arr[r][1] = arr[r-1][0]

print(arr[N][0]+arr[N][1])