'''
Problem Solving Baekjoon 1697
Author: Injun Son
Date: August 15, 2020
'''
import sys
sys.setrecursionlimit(100000)
MAX = 100000
def back_tracking(cur_pos, target_pos, visited_nums, count):
    global ans
    if count> ans:
        visited_nums[cur_pos * 2] = False
        return

    if cur_pos == target_pos:
        ans = min(ans, count)
        return

    else:
        visited_nums[cur_pos]=True
        if cur_pos*2 <=MAX and visited_nums[cur_pos*2] == False and abs(cur_pos - target_pos) > abs(cur_pos*2 - target_pos):
            visited_nums[cur_pos*2] = True
            back_tracking(cur_pos*2, target_pos, visited_nums, count+1)
            visited_nums[cur_pos *2] = False

        if cur_pos-1>=0 and visited_nums[cur_pos-1] == False:
            visited_nums[cur_pos-1] = True
            back_tracking(cur_pos-1, target_pos, visited_nums, count+1)
            visited_nums[cur_pos - 1] = False

        if cur_pos+1<=MAX and visited_nums[cur_pos+1] == False:
            visited_nums[cur_pos+1] = True
            back_tracking(cur_pos+1, target_pos, visited_nums, count+1)
            visited_nums[cur_pos + 1] = False



x, y = map(int, input().split())
ans = abs(x-y)
visited_nums = [False]*(MAX+1)
back_tracking(x, y, visited_nums, 0)
print(ans)