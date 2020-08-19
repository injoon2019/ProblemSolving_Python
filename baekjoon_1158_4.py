'''
Problem Solving Baekjoon 1158_4
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys

N, K = map(int, input().split())
visited = [False]*N
ans_nums = []



print('<', ", ".join(ans_nums), ">", sep="")