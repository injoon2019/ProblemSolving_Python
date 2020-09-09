'''
Problem Solving Baekjoon 5052_2
Author: Injun Son
Date: September 9, 2020
'''
import sys
import math
import sys
input = sys.stdin.readline

def solution(numbers):
    numbers.sort()
    for i in range(len(numbers)-1): #정렬되어있으므로 i번째와 i+1번쨰만 비교해보면된다
        if numbers[i] in numbers[i+1][0:len(numbers[i])]:   #[0:len(numbers[i])]를 안넣으면 반례: 119, 911119
            print("NO")
            return
    print("YES")
    return True


numbers = []
t = int(input())
for i in range(t):
    n = int(input())
    for _ in range(n):
        numbers.append(sys.stdin.readline().strip())
    solution(numbers)
    numbers.clear()
