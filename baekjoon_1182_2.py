'''
Problem Solving Baekjoon 1182_2
Author: Injun Son
Date: August 18, 2020
'''

def make_subseq(now_idx, total_sum,  num_list, s):
    if now_idx >= len(num_list):
        if total_sum ==s:
            return 1

        return 0
    else:
        make_subseq(now_idx+1, total_sum+num_list[now_idx], num_list, s)


n, k = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = make_subseq(0, num_list, 0, s, [])