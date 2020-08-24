'''
Problem Solving Baekjoon 1074
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

def find_count(y, x, size):
    global count
    if size==1:
        return

    if y <= r < y+size//2 and x<= c < x+size//2:
        find_count(y, x, size//2)

    elif y <= r < y+size//2 and x+(size//2)<= c < x+size:
        count += ((size//2)**2)
        find_count(y, x+(size//2), size//2)

    elif y+(size//2)<= r < y+size and x<= c < x+(size//2):
        count += ((size // 2) ** 2)*2
        find_count(y+(size//2), x, size//2)

    elif y+(size//2)<= r < y+size and x+(size//2)<= c < x+size:
        count += ((size // 2) ** 2) * 3
        find_count(y+ (size//2), x + (size // 2), size // 2)


N, r, c = map(int, input().split())
count = 0
find_count(0, 0, 2**N)
# print_board()
print(count)