'''
Problem Solving Baekjoon 15649_3
Author: Injun Son
Date: August 14, 2020
'''

#now_idx 는 몇번째 선택인지를 나타낸다
def back_tracking(now_idx, max_length, length, result, used_list):
    if now_idx < max_length:
        for i in range(1, length+1):
            if not used_list[i]:
                used_list[i] = True
                back_tracking(now_idx+1, max_length, length, result+[i], used_list)
                used_list[i] = False
    else:
        for k in result:
            print(k, end=" ")
        print("")


n, m = map(int, input().split())
used_list = [False]*(n+1)

back_tracking(0, m, n, [], used_list)