'''
Problem Solving Baekjoon 11058
Author: Injun Son
Date: September 18, 2020
'''
import sys
input = sys.stdin.readline
n = int(input())
#각각의 경우에 1번만 눌러도 최소 n번째에는 n개가 있다
dp = [i for i in range(0, 102)]

#dp[5]까지는 그냥 i번씩 A 추가하는게 가장 많다
for i in range(6, 101):
    #한번 전체를 복붙하는데 3스텝 걸린다 (선택, 복사, 붙여넣기)
    # 1. 3단계 전에 것을 선택, 복사, 붙여넣기 하기
    # 2. 4단계 전에 것을 선택, 복사, 붙여넣기, 붙여넣기 하기
    # 3. 5단계 전에 것을 선택, 복사, 붙여넣기, 붙여넣기, 붙여넣기 하기
    dp[i] = max(dp[i-3]*2,dp[i-4]*3, dp[i-5]*4)
print(dp[n])
    