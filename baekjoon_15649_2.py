'''
Problem Solving Baekjoon 15649_2
Author: Injun Son
Date: August 13, 2020
'''
def backt(now_idx, end_idx, length, result, used_list):
    if now_idx < end_idx:
        for i in range(1, length+1):
            if not used_list[i]:
                used_list[i] = True
                backt(now_idx+1, end_idx, length, result+[i], used_list)
                used_list[i] = False
    else:
        for k in result:
            print(k, end=" ")
        print("")

n, m = map(int, input().split())
used_list = [False]*(n+1)

backt(0, m, n, [], used_list)