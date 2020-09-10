'''
Problem Solving Baekjoon 17413_4
Author: Injun Son
Date: September 10, 2020
'''
import sys
from collections import deque

import heapq
import re
S = input()

tmp = re.split(r"<.+?>", S)
tmp2 = re.findall(r"<.+?>", S)
print(tmp)
print(tmp2)
tmp = tmp[1:-1]

#태그가 없는 경우라면
if len(tmp)==0:
    print(' '.join(list(map(lambda x: x[::-1], S.split()))))
else:
    tags = re.findall(r"<.+?>", S)
    print(tags[0]+' '.join(list(map(lambda x:x[::-1], tmp[0].split())))+ tags[1])


'''
input이 <open>gat<close>
일때 tmp = re.findall(r"<.+>", S) 하면 '<open>gat<close>']과 나온다.
문자열 맨끝의 '>' 와 매치가 되기 때문이다.
'?'를 넣으면 최소한의 반복이다.
따라서 tmp2 = re.findall(r"<.+?>", S)는 ['<open>', '<close>'] 를 반환한다
'''