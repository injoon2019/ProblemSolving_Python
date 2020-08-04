'''
Problem Solving Baekjoon 5585
Author: Injun Son
Date: August 3, 2020
'''
import sys
N = int(sys.stdin.readline())
change = 1000 -N
count = 0
coins = [500, 100, 50, 10, 5, 1]
for i in coins:
    count += change // i
    change %= i

print(count)