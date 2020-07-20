'''
Problem Solving Baekjoon 2011
Author: Injun Son
Date: July 19, 2020
'''

alp = ['A', 'B', 'C', 'D', 'E',
       'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O',
       'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'Y',
       'Z']

#
MOD = 1000000
code = input()
dp = [0]*len(code)
dp[0] = 1  #첫번째 글자


if int(code[0])==0:
    print(0)
    exit()

for i in range(1,len(code)):
    dp[i]=dp[i-1]
    if int(code[i-1])==1:
        if i==1:
            dp[i]+=1
        else:
            dp[i]+=dp[i-2]
            dp[i] %= MOD

    elif int(code[i-1])==2:
        if int(code[i])>=0 and int(code[i])<=6:
            if i==1:
                dp[i]+=1
            else:
                dp[i]+=dp[i-2]
                dp[i] %= MOD

    if int(code[i])==0:
        if int(code[i-1])<1 or int(code[i-1])>2:
            print(0)
            exit()
        else:
            if i==1:
                dp[i]-=1
            else:
                dp[i] = dp[i-2]
print(dp[-1])