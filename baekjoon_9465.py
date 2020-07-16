'''
Problem Solving Baekjoon 9465
Author: Injun Son
Date: July 16, 2020
'''

T = int(input())

for i in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
    for j in range(2, n):
        stickers[0][j] += max(stickers[1][j-1], stickers[1][j-2])
        stickers[1][j] += max(stickers[0][j-1], stickers[0][j-2])
    answer = max(stickers[0][-1], stickers[1][-1])
    print(answer)