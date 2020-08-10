'''
Problem Solving Baekjoon 11728
Author: Injun Son
Date: August 10, 2020
'''
N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
index1=0
index2=0
while index1 <len(arr1) and index2 < len(arr2):
    if arr1[index1] <= arr2[index2]:
        print(arr1[index1], end= " ")
        index1 +=1
    else:
        print(arr2[index2], end= " ")
        index2 +=1

while index1 < len(arr1):
    print(arr1[index1], end=" ")
    index1 += 1

while index2< len(arr2):
    print(arr2[index2], end=" ")
    index2 += 1
