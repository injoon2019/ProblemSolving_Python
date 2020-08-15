'''
Problem Solving Baekjoon 1451
Author: Injun Son
Date: August 14, 2020
'''

r, c = map(int, input().split())
table = [list(map(int, list(input()))) for _ in range(r)]
ans = 0

#|||
#중간칸의 가로 인덱스다
for i in range(1, c-1):
    #마지막칸의 가로 인덱스다
    for j in range(i+1, c):
        s1 = sum([table[a][b] for a in range(r) for b in range(i)])
        s2 = sum([table[a][b] for a in range(r) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(r) for b in range(j, c)])
        ans = max(ans, s1*s2*s3)

#  |
# ---
# row의 위치 정하기
for i in range(1,c):
    # column 나눌 위치 정하기. 두칸으로만 나누면된다
    for j in range(1, r):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, c)])
        s3 = sum([table[a][b] for a in range(j, r) for b in range(c)])
        ans = max(ans, s1 * s2 * s3)

#---
# |
for i in range(1, r):
    for j in range(1, c):
        s1 = sum([table[a][b] for a in range(i) for b in range(c)])
        s2 = sum([table[a][b] for a in range(i, r) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, r) for b in range(j, c)])
        ans = max(ans, s1 * s2 * s3)

# -|
for i in range(1, r):
    for j in range(1, c):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, r) for b in range(j)])
        s3 = sum([table[a][b] for a in range(r) for b in range(j, c)])
        ans = max(ans, s1 * s2 * s3)

#|-
for i in range(1, r):
    for j in range(1, c):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, c)])
        s2 = sum([table[a][b] for a in range(i, r) for b in range(j, c)])
        s3 = sum([table[a][b] for a in range(r) for b in range(j)])
        ans = max(ans, s1 * s2 * s3)

#=
for i in range(1, r-1):
    for j in range(i+1, r):
        s1 = sum([table[a][b] for a in range(i) for b in range(c)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(c)])
        s3 = sum([table[a][b] for a in range(j, r) for b in range(c)])
        ans = max(ans, s1 * s2 * s3)

print(ans)