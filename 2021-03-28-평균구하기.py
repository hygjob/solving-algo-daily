# 2021.3.28
# 평균구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    alen = len(arr)
    sum = 0
    for i in range(alen):
        sum += arr[i]
    answer = sum / alen
        
    return answer
