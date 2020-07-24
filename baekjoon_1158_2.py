'''
Problem Solving Baekjoon 1158
Author: Injun Son
Date: July 24, 2020
'''
n,m = map(int, input().split())
l = list(range(1, n+1))
r = []
index = 0

while l:
    index = (index + m -1) % len(l)
    r.append(str(l.pop(index)))

print('<', ", ".join(r), ">", sep="")

'''
list도 while을 쓸 수 있다. 크기가 남아있는동안
list.pop(index) 가능하다
string join 사용법 
'''