'''
Problem Solving Baekjoon 2143_2
Author: Injun Son
Date: September 18, 2020
'''

T = int(input())
n = int(input())
arr_a = list(map(int, input().split()))
m = int(input())
arr_b = list(map(int, input().split()))

a_sums = dict()
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr_a[j]
        if tmp in a_sums:
            a_sums[tmp] +=1
        else:
            a_sums[tmp] = 1

b_sums = dict()
for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += arr_b[j]
        if tmp in b_sums:
            b_sums[tmp] += 1
        else:
            b_sums[tmp] = 1


ans = 0

for i, key in enumerate(a_sums):
    if T-key in b_sums:
        ans += a_sums[key]*b_sums[T-key]

print(ans)
