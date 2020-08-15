'''
Problem Solving Baekjoon 10819
Author: Injun Son
Date: August 14, 2020
'''
import sys
import copy
sys.setrecursionlimit(10000)

permutation_list = []

def back_tracking(cur_count, max_count, result, used_list):
    if cur_count == max_count:
        permutation_list.append(result)

    if cur_count < max_count:
        for i in range(0, max_count):
            if arr[i] in possible_nums:
                possible_nums.remove(arr[i])
                back_tracking(cur_count+1, max_count, result+[arr[i]], used_list)
                possible_nums.append(arr[i])



N = int(input())
arr = list(map(int, input().split()))
used_list = [False]*(200+2)
possible_nums = copy.deepcopy(arr)
back_tracking(0, N, [], used_list)
answer = 0
# print(permutation_list)
for list in permutation_list:
    sum = 0
    for i in range(0, len(list)-1):
        sum += abs(list[i]-list[i+1])
    answer = max(sum, answer)

print(answer)

'''
처음에는 단순 순열로 풀려고 했고, 반례는 -5, 0, -4, -3, -3, -2에 대응하지 못했다
이유는 boolean type의 used_list를 만들어 씀으로서, 한번 -3을 쓰면 다시 쓰지 않기 때문에.
'''