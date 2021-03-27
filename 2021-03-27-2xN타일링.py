# 2*n 타일링
# 2021.3.27
# https://programmers.co.kr/learn/courses/30/lessons/12900

def modify_fibonacci(num): 
    a, b = 1, 1
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 2
    for i in range(0, num): 
        a, b = b, a+b 
    a = a  % 1000000007
    return a


def solution(n):
    answer = modify_fibonacci(n)
    return answer
