'''
Problem Solving Baekjoon 1924
Author: Injun Son
Date: July 14, 2020
'''
import sys
import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x,y = map(int, input().split())
answer = datetime.date(2007, x, y).weekday()
print(days[answer])
