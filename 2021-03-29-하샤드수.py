# 하샤드 수
# 2021.3.29
# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    sx = str(x)
    sum_of_digit = 0
    
    for i in range(len(sx)):
        sum_of_digit += int(sx[i])
        
    r = x % sum_of_digit
    if (r == 0):
        answer = True
    else:
        answer = False        
    
    return answer
