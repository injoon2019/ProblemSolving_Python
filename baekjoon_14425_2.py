'''
Problem Solving Baekjoon 14425
Author: Injun Son
Date: September 9, 2020
'''
import sys
import math
import sys
#트라이 알고리즘으로 풀기
#https://developmentdiary.tistory.com/459

input = sys.stdin.readline
# 트라이 구조에 필요한 노드
class Node:
    def __init__(self, chr):
        self.chr = chr
        self.child = {}
        self.check = False

#해당 문자열 있는지 확인
def triedfs(node, s, n):
    if len(s)==n: #문자열의 끝까지 같으면
        if node.check: #문자열 끝표시가 있으면
            result.append(s)
            return
        else:
            return
    if s[n] in node.child: #재귀를 통해 확인
        triedfs(node.child[s[n]], s, n+1)
    return

#trie 구조
trie = Node('')
N, M = map(int, input().split())
for _ in range(N):
    tmp = trie
    s = input().rstrip()
    for i in s: #문자열 추가
        if i in tmp.child: #해당 문자가 있다면
            tmp = tmp.child[i] #해당 문자의 노드로 이동
            if i==s[-1]:
                tmp.check=True

        else:
            a = Node(i)
            tmp.child[i] = a
            tmp = a
            if i == s[-1]: #문자 끝표시
                tmp.check = True

count = 0
result = []
for _ in range(M):
    p = input().rstrip()
    triedfs(trie, p, 0)

print(len(result))