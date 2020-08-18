'''
Problem Solving Baekjoon 1963
Author: Injun Son
Date: August 18, 2020
'''
import sys
from collections import deque
import math


def Erathos():
    for i in range(2, int(math.sqrt(10001))+1):
        for j in range(i*2, 10001, i):
            prime_numbers[j] = False

def find_possible_nums(num):
    temp_num = str(num)
    global possible_nums
    #1의 자리
    for i in range(0, 10):
        if i != (int(temp_num[3])) and prime_numbers[int(temp_num[0:3]+str(i))]==True:
            possible_nums.append(int(temp_num[0:3]+str(i)))
    #10의 자리
    for i in range(0, 10):
        if i != (int(temp_num[2])) and prime_numbers[int(temp_num[0:2]+str(i)+temp_num[-1])]==True:
            possible_nums.append(int(temp_num[0:2]+str(i)+temp_num[-1]))
    #100의 자리
    for i in range(0, 10):
        if i != (int(temp_num[1])) and prime_numbers[int(temp_num[0:1]+str(i)+temp_num[2:])]==True:
            possible_nums.append(int(temp_num[0:1]+str(i)+temp_num[2:]))
    #1000의 자리
    for i in range(1, 10):
        if i != (int(temp_num[0])) and prime_numbers[int(str(i)+temp_num[1:])]==True:
            possible_nums.append(int(str(i)+temp_num[1:]))


def solve():
    global possible_nums
    while q:
        cur = q.popleft()
        if cur == target:
            return visited_nums[cur]
        else:
            possible_nums = []
            find_possible_nums(cur)
            # print(possible_nums)
            for i in possible_nums:
                nextPos(i, cur)

def nextPos(nex, cur):
    if visited_nums[nex] > visited_nums[cur]+1:
        visited_nums[nex] = visited_nums[cur]+1
        q.append(nex)

prime_numbers=[True]*10001
Erathos()
T = int(input())
MAX = sys.maxsize
possible_nums= []
for _ in range(T):
    m, target = map(int, input().split())
    visited_nums = [MAX]*10001
    visited_nums[m]=0
    min_count = 0
    q = deque([m])
    print(solve())