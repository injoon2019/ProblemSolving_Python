'''
Problem Solving Baekjoon 17413_2
Author: Injun Son
Date: August 22, 2020
'''
import sys
n = input().split('<')
s= ''
for words in n:
    if '>' in words:
        words2 = words.split(">")
        s += "<"+words2[0]+">"+" ".join(map(lambda t: t[::-1], words2[1].split()))
    else:
        s+=' '.join(map(lambda t: t[::-1], words.split()))
print(s)
