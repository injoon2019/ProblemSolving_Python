'''
Problem Solving Baekjoon 9095_2
Author: Injun Son
Date: August 14, 2020
'''
def back_tracking(cur_sum, max_sum):
    global count
    if cur_sum == max_sum:
        count +=1
        return
    elif cur_sum > max_sum:
        return
    else:
        for i in range(1, 4):
            back_tracking(cur_sum+i, max_sum)

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    back_tracking(0, n)
    print(count)