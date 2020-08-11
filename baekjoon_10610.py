'''
Problem Solving Baekjoon 10610
Author: Injun Son
Date: August 11, 2020
'''
import sys
number = list(input())
sum = 0
for i in number:
    sum += int(i)

if sum % 3!=0:
    print("-1")
    exit()
try:
    zero_index = number.index("0")
except:
    print("-1")
    exit()
number2= number[0:zero_index]+number[zero_index+1:]+["0"]
number2.sort()
for i in range(len(number2)-1, -1, -1):
    print(number2[i], end="")
