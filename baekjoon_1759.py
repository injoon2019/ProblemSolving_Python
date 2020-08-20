'''
Problem Solving Baekjoon 1759
Author: Injun Son
Date: August 20, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
used_list = [False]*27
def back_tracking(cur_count, max_count, used_list, vowels, consonants, result, prev):
    if cur_count== max_count and consonants>=2 and vowels>=1:
        for c in result:
            print(c, end="")
        print("")
    else:
        for i in range(len(arr)):
            if used_list[ord(arr[i])-ord('a')]==False and arr[i]> prev:
                used_list[ord(arr[i])-ord('a')]=True
                new_vowels = vowels
                new_consonants = consonants
                if arr[i] in ['a', 'e', 'i', 'o', 'u']:
                    new_vowels+=1
                else:
                    new_consonants+=1

                back_tracking(cur_count+1, max_count, used_list, new_vowels, new_consonants, result+[arr[i]], arr[i])
                used_list[ord(arr[i])-ord('a')] = False

back_tracking(0, L, used_list, 0, 0, [], '0')