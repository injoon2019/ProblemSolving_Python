'''
Problem Solving Baekjoon 15655
Author: Injun Son
Date: August 14, 2020
'''
def back_tracking(cur_count, max_count, input_arr, result, used_list):
    if cur_count < max_count:
        for i in range(len(input_arr)):
            if not used_list[i]:
                back_tracking(cur_count+1, max_count, input_arr, result+[input_arr[i]], used_list)
    else:
        for k in result:
            print(k, end=" ")
        print("")

n, m = map(int, input().split())
input_arr = list(map(int, input().split()))
input_arr.sort()
used_list = [False]*(10001)
back_tracking(0, m, input_arr, [], used_list)