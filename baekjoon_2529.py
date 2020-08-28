'''
Problem Solving Baekjoon 2529
Author: Injun Son
Date: August 27, 2020
'''

K = int(input())
equality_signs = input()
equality_signs = equality_signs.replace(" ", "")
equality_signs =equality_signs+" "
used_list = [False]*10
ans_list = []
def back_tracking(cur_num, max_num, used_list, result, prev_condition, prev_val):
    if cur_num == max_num:
        ans_list.append(result)

    else:
        for i in range(10):
            if used_list[i]==False:
                if prev_val is None:
                    used_list[i] = True
                    back_tracking(cur_num + 1, max_num, used_list, result +[i], equality_signs[cur_num], i)
                    used_list[i] = False
                else:
                    if prev_condition=="<":
                        if prev_val < i:
                            used_list[i]=True
                            back_tracking(cur_num+1, max_num, used_list, result+[i], equality_signs[cur_num], i)
                            used_list[i]=False
                    else:
                        if prev_val > i:
                            used_list[i]=True
                            back_tracking(cur_num+1, max_num, used_list, result+[i], equality_signs[cur_num], i)
                            used_list[i]=False

back_tracking(0, K+1, used_list, [], "", None)
biggest = ans_list[-1]
smallest = ans_list[0]
print(''.join(str(e) for e in biggest))
print(''.join(str(e) for e in smallest))
