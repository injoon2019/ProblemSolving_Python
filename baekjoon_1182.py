'''
Problem Solving Baekjoon 1182
Author: Injun Son
Date: August 18, 2020
'''
N, S = map(int, input().split())
arr = list(map(int, input().split()))
possible_lists = []
def back_tracking(cur_count, max_count, result):
    if cur_count == max_count:
        possible_lists.append(result)

    else:
        back_tracking(cur_count+1, max_count, result+[arr[cur_count]])
        back_tracking(cur_count + 1, max_count, result)

back_tracking(0, N, [])
ans = 0
for list in possible_lists:
    if len(list)>0 and sum(list)==S:
       ans +=1

print(ans)