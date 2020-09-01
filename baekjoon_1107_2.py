'''
Problem Solving Baekjoon 1107_2
Author: Injun Son
Date: September 1, 2020
'''

target = int(input())
M = int(input())
broken_buttons = []
if M !=0:
    broken_buttons = list(map(int, input().split()))
remote = [ abs(100-i) for i in range(0, 1000001)]

def numbers_available(num):
    str_num = str(num)
    for i in str_num:
        if int(i) in broken_buttons:
            return False
    return True

for i in range(0, 1000001):
    if numbers_available(i):
        remote[i] = min(remote[i], len(str(i)))

for i in range(0, 1000001):
    if i != target:
        remote[target] = min(remote[target], abs(i-target)+remote[i])

print(remote[target])