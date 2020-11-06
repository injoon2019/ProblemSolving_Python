'''
Problem Solving Baekjoon 1213
Author: Injun Son
Date: November 6, 2020
'''
import sys
from collections import Counter

name = list(input())
alphabets = [0]*26
odd_count = 0
for char in name:
    alphabets[ord(char)-ord('A')]+=1

ans = ''
mid_char = None
for i in range(26):
    if (alphabets[i]%2) != 0:
        odd_count +=1
    if odd_count > 1:
        print("I'm Sorry Hansoo")
        exit()
    elif alphabets[i] > 0:
        if alphabets[i] %2 == 1:
            ans += chr(i+ord('A')) * (alphabets[i] //2)
            mid_char = chr(i+ord('A'))
        else:
            ans += chr(i+ord('A')) * (alphabets[i] //2)

if odd_count:
    late = ans[::-1]
    ans += mid_char
    ans += late
else:
    ans += ans[::-1]
print(ans)