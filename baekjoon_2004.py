'''
Problem Solving Baekjoon 2004
Author: Injun Son
Date: July 26, 2020
'''
import sys
import math

n, m = map(int, input().split())
r = n-m
five = 5
two = 2
n_f = m_f = r_f = 0
n_t = m_t = r_t = 0
while five <= 2000000000:
    n_f += n//five
    m_f += m//five
    r_f += r//five
    five *=5

while two <= 2000000000:
    n_t += n//two
    m_t += m//two
    r_t += r//two
    two *=2

print(min(n_f - m_f - r_f, n_t - m_t -r_t))