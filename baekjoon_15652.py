'''
Problem Solving Baekjoon 15652
Author: Injun Son
Date: August 14, 2020
'''
def back_tracking(cur_count, max_count, length, result, used_list, prev):
    if cur_count<max_count:
        for i in range(1, length+1):
            if i >= prev:
                back_tracking(cur_count+1, max_count, length, result+[i], used_list, i)
    else:
        for k in result:
            print(k, end= " ")
        print("")

n, m = map(int, input().split())
used_list = [False]*(n+1)

back_tracking(0, m, n, [], used_list, 0)