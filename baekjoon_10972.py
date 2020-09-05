'''
Problem Solving Baekjoon 10972
Author: Injun Son
Date: September 5, 2020
'''
from collections import deque
import sys
from itertools import combinations

'''
1. a[k] < a[k+1]가 성립하는 k의 최대 값을 찾는다
   (여기서 k값이 존재하지 ㅇ낳는다면 이미 내림차순으로 정렬되어있다는 뜻으로, 가능한 순열에서 가장 큰 값이다)
2. 인덱스 k 이후의 값들 중 a[k] < a[m]이 성립하는 m의 최대값을 찾는다
3. k와 m 자리의 값을 서로 바꾸어 준다
4. 인덱스 k 이후의 값들을 오름차순으로 정렬해준다 
'''

'''
a = [3,5,6,4,2,1]의 다음 사전식으로 오는 순열을 구해보자
(정답은 [3,6,1,2,4,5]
1. a 배열에서 a[k] < a[k+1]이 성립되는 k는 0과 1이다. 여기서 최대값을 구해야되니 k는 1이된다
2. a[1] = 5이다. 인덱스가 1이후에서 5보다 큰 수는 6뿐이니 m은 2가 된다
3. a[k]와 a[m]의 값을 서로 바꾸어 준다 => a = [3,6,5,4,2,1]
4. k 이후의 값들을 오름차순으로 정렬한다 => a = [3,6,1,2,4,5]
'''

n = int(input())
seq = list(map(int, input().split()))

k = -1
#1. k의 최대값 구하기
for i in range(len(seq)-1):
    if seq[i] < seq[i+1]:
        k = i 

#이미 가장 큰 수일 경우
if k==-1:
    print(-1)

else:
    # 2. m의 최대값 구하기
    for j in range(k+1, len(seq)):
        if seq[k] < seq[j]:
            m = j

    #3. k와 m의 값 바꿔치기
    seq[k], seq[m] = seq[m], seq[k]

    #4. k 이후 정렬
    tmp = seq[k+1:]
    tmp.sort()
    answer = seq[:k+1]+tmp

    for num in answer:
        print(num, end=" ")
    print()