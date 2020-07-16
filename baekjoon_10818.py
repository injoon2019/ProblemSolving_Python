'''
Problem Solving Baekjoon 10818
Author: Injun Son
Date: July 14, 2020
'''
import sys
import datetime

N = int(input())
lst = list(map(int, input().split()))
print(min(lst), max(lst))

'''
여러 값을 한번에 list로 받을때는 list로 캐스팅해줘야한다
'''