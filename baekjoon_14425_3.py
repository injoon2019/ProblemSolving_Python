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
#트라이 노드
class Node:
    def __init__(self, char):
        self.char = char
        self.child = {}
        self.endCheck = False

#해당 문자열이 있는지 확인
def triedfs(node, s, n):
    if len(s)==n:
        if node.endCheck:
            result.append(s)
            return
        else:
            return
    if s[n] in node.child:
        triedfs(node.child[s[n]], s, n+1)
    return


#trie 구조
trie = Node('')
N, M = map(int, input().split())
for _ in range(N):
    tmp = trie
    word = input().rstrip()
    for i in range(len(word)):
        if word[i] in tmp.child:
            tmp = tmp.child[word[i]]
            if i == len(word)-1:
                tmp.endCheck = True

        else:
            a = Node(word[i])
            tmp.child[word[i]] = a
            tmp = a
            if i==len(word)-1:
                tmp.endCheck = True

result = []
for _ in range(M):
    p = input().rstrip()
    triedfs(trie, p, 0)

print(len(result))
