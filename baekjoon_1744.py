'''
Problem Solving Baekjoon 1744
Author: Injun Son
Date: August 12, 2020
'''
#세로 길이 N와 가로 길이 M
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
sum = 0
i = 0
while i < len(arr):
    if i == len(arr)-1:
       sum += arr[i]
       i+=1
    else:
        if arr[i]< 0 and arr[i+1]<0:
            sum += arr[i] * arr[i+1]
            i+=2
        elif arr[i]< 0 and arr[i+1]==0:
            sum += arr[i] * arr[i+1]
            i+=2
        elif arr[i]< 0 and arr[i+1]>0:
            sum += arr[i]
            i+=1
        elif arr[i]== 0 and arr[i+1]>=0:
            sum += arr[i]
            i+=1
        elif arr[i]> 0 and arr[i+1]>0:
            if (len(arr)-1-i)%2 ==1 and arr[i]!=1:
                sum += arr[i] * arr[i + 1]
                i += 2
            else:
                sum += arr[i]
                i += 1
print(sum)