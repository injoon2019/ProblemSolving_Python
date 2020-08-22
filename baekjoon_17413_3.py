'''
Problem Solving Baekjoon 17413_3
Author: Injun Son
Date: August 22, 2020
'''
import sys
sentence_split = input().split("<")
s=''
for words in sentence_split:
    # <>가 있는 경우
    if ">" in words:
        words2 = words.split(">")
        s += '<'+words2[0]+">"+ " ".join(map(lambda x: x[::-1], words2[1].split()))
    else:
        s+= ' '.join(map(lambda x: x[::-1], words.split()))

print(s)