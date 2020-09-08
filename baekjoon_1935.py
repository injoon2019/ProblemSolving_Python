'''
Problem Solving Baekjoon 1935
Author: Injun Son
Date: September 8, 2020
'''
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
sentence = sys.stdin.readline().rstrip()
nums = [0]*26
stack = []
for i in range(N):
    a = int(input())
    nums[i] = a

def calculate(a, b, ch):
    a = float(a)
    b = float(b)
    if ch=='+':
        return a+b
    elif ch=='-':
        return a-b
    elif ch=='/':
        return a/b
    elif ch=='*':
        return a*b

for ch in sentence:
    if ch not in ['+', '-', '/', '*']:
        stack.append(nums[ord(ch)-ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, b, ch))

print('%0.2f' % stack.pop())

'''
후위 표기식이 주어졌을때 계산하는 방법
소수점 n번째 자리까지 출력하는 방법
'''