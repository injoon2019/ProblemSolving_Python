'''
Problem Solving Programmers winter_coding_2
Author: Injun Son
Date: October 31, 2020
'''
import math
from itertools import combinations
from collections import deque

def solution(encrypted_text, key, rotation):
    answer = ''
    ans_deque = deque()

    for char in encrypted_text:
        ans_deque.append(char)

    #다시 역으로 되돌린다
    ans_deque.rotate(-rotation)
    rotate_backed = list(ans_deque)

    alphabets = [chr(char) for char in range(ord('a'), ord('z')+1)]

    for i in range(len(encrypted_text)):
        if (ord(rotate_backed[i])-ord('a')) - (ord(key[i])- ord('a')+1) <= -27:
            rotate_backed[i] = alphabets[(ord(rotate_backed[i])-ord('a')) - (ord(key[i])- ord('a')+1) + 26]
        else:
            rotate_backed[i] = alphabets[(ord(rotate_backed[i])-ord('a')) - (ord(key[i])-ord('a')+1)]
    return ''.join(rotate_backed)

print(solution("qyyigoptvfb", "abcdefghijk", 3))