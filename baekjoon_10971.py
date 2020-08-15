'''
Problem Solving Baekjoon 10971
Author: Injun Son
Date: August 15, 2020
'''
import sys
sys.setrecursionlimit(100000)
def back_tracking(cur_count, max_count, result, used_list):
    global permutation_list
    if cur_count==max_count:
        permutation_list.append(result+[result[0]])
        return

    if cur_count < max_count:
        for i in range(max_count):
            if not used_list[i]:
                used_list[i]=True
                back_tracking(cur_count+1, max_count, result+[i], used_list)
                used_list[i]= False


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
order = [i for i in range(0, N)]
used_list = [False]*(N)
permutation_list = []
back_tracking(0, N, [], used_list)
answer = sys.maxsize
for list in permutation_list:
    temp_sum = 0
    for i in range(len(list)-1):
        if graph[list[i]][list[i+1]] == 0:
            print(list)
            break
        else:
            temp_sum += graph[list[i]][list[i+1]]
    answer = min(temp_sum, answer)
print(answer)