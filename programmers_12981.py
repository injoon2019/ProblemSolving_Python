'''
Problem Solving Programmers 12981 영어 끝말잇기
Author: Injun Son
Date: September 8, 2020
'''
import math

def solution(n, words):
    answer = [0,0]
    word_set = set()
    index = 0
    prev_word = None
    while index < len(words):
        # print(prev_word, words[index])
        if prev_word is None:
            prev_word = words[index]

        elif prev_word[-1] != words[index][0]:
            return [(index%n)+1 , math.ceil((index+1)/n)]

        if words[index] in word_set:
            return [(index%n)+1 , math.ceil((index+1)/n)]

        word_set.add(words[index])
        prev_word = words[index]
        index +=1


    return answer

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))