'''
Problem Solving Baekjoon 15657
Author: Injun Son
Date: August 27, 2020
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def back_tracking(cur_num, max_num, result, prev):
    if cur_num==max_num:
        for i in result:
            print(i, end=" ")
        print("")

    else:
        for i in arr:
            if i >=prev:
                back_tracking(cur_num+1, max_num, result+[i], i)

back_tracking(0, M, [], 0)