'''
Problem Solving Baekjoon 10952
Author: Injun Son
Date: July 13, 2020
'''

while True:
    try:
        a,b = map(int, input().split())
        if(a==0 and b==0):
            break
        print(a+b)
    except:
        break


'''
map( ) 사용 시 일괄적인 형 변환이 가능하다
'''
