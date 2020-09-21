'''
Problem Solving Baekjoon 14881
Author: Injun Son
Date: September 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
import math

'''
https://elwlsek.tistory.com/725
https://namu.wiki/w/%EC%9B%90%ED%95%98%EB%8A%94%20%EB%AC%BC%EC%9D%98%20%EC%96%91%20%EC%96%BB%EA%B8%B0
a 와 b의 최대공약수가 c의 약수이고 c가 a,b의 최대값 이하이면 만들 수 있다
'''

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    gcd = math.gcd(a, b)
    if c%gcd==0 and c<=max(a, b):
        print("YES")
    else:
        print("NO")