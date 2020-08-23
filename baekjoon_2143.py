'''
Problem Solving Baekjoon 2143
Author: Injun Son
Date: August 22, 2020
'''
T = int(input())
n = int(input())
a_arr = list(map(int, input().split()))
m = int(input())
b_arr = list(map(int, input().split()))

a_dict =  dict()
b_dict =  dict()

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a_arr[j]
        if not a_dict.get(sum):
            a_dict[sum] =1
        else:
            a_dict[sum] +=1

for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += b_arr[j]
        if not b_dict.get(sum):
            b_dict[sum] =1
        else:
            b_dict[sum] +=1

ans = 0

for _,key in enumerate(a_dict):
    if b_dict.get(T-key):
        ans += (a_dict[key]*b_dict[T-key])

print(ans)

