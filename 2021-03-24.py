# 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937
# 2021.3.24

def solution(num):
    answer = ''
    if num %2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
