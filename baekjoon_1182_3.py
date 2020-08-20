'''
Problem Solving Baekjoon 1182_3
Author: Injun Son
Date: August 20, 2020
'''
def back_tracking(cur_index, max_length, result):
    global ans
    if cur_index== max_length:
        if sum(result)==S and len(result)> 0:
            ans+=1
        return
    else:
        back_tracking(cur_index+1, max_length, result+[arr[cur_index]])
        back_tracking(cur_index + 1, max_length, result)

N, S = map(int, (input().split()))
arr = list(map(int, input().split()))
ans = 0
back_tracking(0,N, [])
print(ans)