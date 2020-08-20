'''
Problem Solving Baekjoon 2003
Author: Injun Son
Date: August 20, 2020
'''
def solve(cur_index, sum):
    global ans
    if cur_index==N:
        return
    if arr[cur_index]+sum==S:
        ans+=1
    else:
        sum += arr[cur_index]
        solve(cur_index+1, sum)

N, S = map(int, (input().split()))
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    solve(i, 0)
print(ans)