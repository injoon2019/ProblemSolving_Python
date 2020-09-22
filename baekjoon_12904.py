'''
Problem Solving Baekjoon 12904
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
S = input()
T = input()

'''
거꾸로 생각하기 
T의 맨 마지막에 A가 있는 것은, 그 앞에 어떻게든 잘 만들어와서, A를 추가한 것이다
T의 맨 마지막에 A가 있는 것은, 그 앞에 어떻게든 잘 만들어와서, 뒤집고 B를 추가한 것이다. 
그렇게 뒤에서부터 추적해서 S가 나오면 만들 수 있는 것이다 
'''

while len(S)!=len(T):
    if T[-1]=='A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

print(1 if S==T else 0)