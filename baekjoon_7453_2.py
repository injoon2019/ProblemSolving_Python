'''
Problem Solving Baekjoon 7453_2
Author: Injun Son
Date: September 16, 2020
'''
import sys

input = sys.stdin.readline
n = int(input())
a = []; b = []; c = []; d = []

for i in range(n):
    A, B, C ,D = map(int, input().split())
    a.append(A); b.append(B); c.append(C); d.append(D)

ab = dict()
cd = dict()

for a_ in a:
    for b_ in b:
        if not ab.get(a_ + b_):
            ab[a_+b_] = 1
        else:
            ab[a_+b_] +=1

for c_ in c:
    for d_ in d:
        if not cd.get(c_ + d_):
            cd[c_+d_] = 1
        else:
            cd[c_+d_] +=1

count = 0
for _, key in enumerate(ab):
    if cd.get(-key):
        count += (ab[key]*cd[-key])

print(count)