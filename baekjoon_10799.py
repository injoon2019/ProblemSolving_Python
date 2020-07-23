'''
Problem Solving Baekjoon 10799
Author: Injun Son
Date: July 23, 2020
'''
import sys
str = sys.stdin.readline()
stack = []

count = 0
for i in range(len(str)):
    if str[i]=="(":
        stack.append("(")
    else:
        if str[i-1]=="(":
            stack.pop()
            count += len(stack)
        else:
            if len(stack)>0:
                stack.pop()
                count +=1

    #print(i, len(stack), count)
print(count)
