'''
Problem Solving Baekjoon 2632
Author: Injun Son
Date: August 22, 2020
'''
T = int(input())
m, n = map(int, input().split())
a_arr = [int(input()) for _ in range(m)]
b_arr = [int(input()) for _ in range(n)]

a_dict= {}
b_dict= {}

for i in range(0, m):
    a_sum = 0
    for j in range(0, m):
        k = (i+j)%m
        a_sum += a_arr[k]

        if a_dict.get(a_sum):
            a_dict[a_sum]+=1
        else:
            a_dict[a_sum]=1

a_sum = sum(a_arr)
a_dict[a_sum]=1

for i in range(0, n):
    b_sum = 0
    for j in range(0, n):
        k = (i+j)%n
        b_sum += b_arr[k]
        # print(b_sum, end=" ")
        if b_dict.get(b_sum):
            b_dict[b_sum]+=1
        else:
            b_dict[b_sum]=1

b_sum = sum(b_arr)
b_dict[b_sum]=1

ans = 0
for _, key in enumerate(a_dict):
    if b_dict.get(T-key):
        ans += (a_dict[key])*(b_dict[T-key])

if a_dict.get(T):
    ans += a_dict[T]

if b_dict.get(T):
    # print("b_dict[T]", b_dict[T])
    ans+= b_dict[T]

print(ans)
