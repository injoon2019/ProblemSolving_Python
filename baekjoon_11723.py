'''
Problem Solving Baekjoon 11723
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq
input = sys.stdin.readline
M = int(input())
empty_set = set()
for _ in range(M):
    commands = list(input().split())
    if commands[0]=="add":
        empty_set.add(int(commands[1]))
    if commands[0]=="remove" and int(commands[1]) in empty_set:
        empty_set.remove(int(commands[1]))
    if commands[0]=="check":
        if int(commands[1]) in empty_set:
            print("1")
        else:
            print("0")
    if commands[0]=="toggle":
        if int(commands[1]) in empty_set:
            empty_set.remove(int(commands[1]))
        else:
            empty_set.add(int(commands[1]))
    if commands[0]=="all":
        empty_set = set(range(1, 21))
    if commands[0]=="empty":
        empty_set.clear()