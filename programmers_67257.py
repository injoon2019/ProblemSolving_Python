'''
Problem Solving Programmers 67257
Author: Injun Son
Date: September 8, 2020
'''

expression = "100-200*300-500+20"
answer = 0
def calculate(a,b,op):
    if op=='+':
        return a+b
    elif op=="*":
        return a*b
    else:
        return a-b

def solution(expression):
    import re
    from itertools import permutations
    priors = list(permutations(["+", "*", "-"], 3))
    digit_pattern = re.compile("[0-9]+")
    operator_pattern = re.compile("[^0-9]")
    numbers = list(map(int, digit_pattern.findall(expression)))
    operators = list(operator_pattern.findall(expression))

    global answer
    for pr in priors:
        number = numbers
        ope = operators
        for i in range(3):
            stack = [number[0]]
            stack_op = []
            count = 1
            while count < len(number):
                stack.append(number[count])
                stack_op.append(ope[count-1])
                count +=1
                if stack_op[-1]==pr[i]:
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    op = stack_op.pop(-1)

                    stack.append(calculate(a,b,op))
            number = stack
            ope = stack_op
        answer = max(answer, abs(number[0]))
    return answer

print(solution(expression))
