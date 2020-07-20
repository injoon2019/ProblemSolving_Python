'''
Problem Solving Baekjoon 10825
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = []
for i in range(N):
    name, kor, eng, math = input().split(" ")
    arr.append((name, int(kor), int(eng), int(math)))

ans = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in ans:
    print(i[0])