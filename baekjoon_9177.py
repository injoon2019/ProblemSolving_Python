'''
Problem Solving Baekjoon 9177
Author: Injun Son
Date: November 6, 2020
'''
import sys
from collections import Counter

find_flag = False

def test(word1, word2, word3):
    alphabet = [0]*200
    for i in range(len(word1)):
        if word1[i].isupper():
            alphabet[ord(word1[i]) - ord('A')]+=1
        else:
            alphabet[ord(word1[i]) - ord('a')]+=1

    for i in range(len(word2)):
        if word2[i].isupper():
            alphabet[ord(word2[i]) - ord('A')]+=1
        else:
            alphabet[ord(word2[i]) - ord('a')]+=1

    for i in range(len(word3)):
        if word3[i].isupper():
            alphabet[ord(word3[i]) - ord('A')] -=1
        else:
            alphabet[ord(word3[i]) - ord('a')] -=1

    for i in range(200):
        if alphabet[i] != 0:
            return False
    return True

def dfs(index1, index2, index3, word1, word2, target):
    global find_flag

    if find_flag:
        return
    if index3 == len(target):
        find_flag = True
        return

    if index1 < len(word1):
        if word1[index1] == target[index3]:
            dfs(index1+1, index2, index3+1, word1, word2, target)
    if index2 < len(word2):
        if word2[index2] == target[index3]:
            dfs(index1, index2+1, index3+1, word1, word2, target)


N = int(input())
for i in range(N):
    find_flag = False
    words = input().split()
    if (test(words[0], words[1], words[2])):
        dfs(0, 0, 0, words[0], words[1], words[2])
    if find_flag:
        print("Data set {}: yes".format(i+1))
    else:
        print("Data set {}: no".format(i + 1))