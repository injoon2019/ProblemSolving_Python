'''
Problem Solving Baekjoon 15663
Author: Injun Son
Date: August 27, 2020
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans_set = set([])
used_list = [False]*(N)
def back_tracking(cur_num, max_num, used_list, result):
    if cur_num == max_num:
        ans_set.add(tuple(result))

    else:
        for i in range(len(arr)):
            if used_list[i]==False:
                used_list[i]=True
                back_tracking(cur_num+1, max_num, used_list, result+[arr[i]])
                used_list[i]=False

back_tracking(0, M, used_list, [])
ans_list = list(ans_set)
ans_list.sort()
for i in ans_list:
    for k in i:
        print(k, end=" ")
    print("")