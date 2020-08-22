'''
Problem Solving Baekjoon 17413
Author: Injun Son
Date: August 22, 2020
'''
import sys
from heapq import heappush, heappop
sentence = input()
sentence +="$"
sentence_split= []
tmp_word =""
tag_start = False
for i in range(len(sentence)):
    if sentence[i]=="<":
        sentence_split.append(tmp_word)
        tag_start=True
        tmp_word = ""
        tmp_word +=sentence[i]

    elif sentence[i]==">":
        tag_start=False
        tmp_word+=sentence[i]
        sentence_split.append(tmp_word)
        tmp_word=""

    elif sentence[i]==" " or sentence[i]=="$":
        if tag_start:
            tmp_word += sentence[i]
        else:
            sentence_split.append(tmp_word)
            tmp_word=""
            sentence_split.append(" ")

    else:
        tmp_word += sentence[i]

for word in sentence_split:
    if word != '':
        if word[0]!="<":
            for i in range(len(word)-1, -1, -1):
                print(word[i],end="")
        else:
            for i in range(len(word)):
                print(word[i], end="")


