'''
Problem Solving Baekjoon 1588
Author: Injun Son
Date: August 5, 2020
'''
#1은 132로 바뀌고, 2는 211로 바뀌고, 3은 232로 바뀐다.
start = input()
left = input()
right = input()
N = int(input())
str = start
dict = {'1':'132', '2':'211', '3':'232'}
arr= ['1', '2', '3']

def check():
    check_list = []
    if '1' in str:
        check_list.append('1')
    if '2' in str:
        check_list.append('2')
    if '3' in str:
        check_list.append('3')
    return check_list


for _ in range(N):
    check_list = check()
    for i in check_list:
        str = str.replace(i, dict[i])
        print(str)

print(str)
