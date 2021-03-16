# 제목: 약수의 합
# 2021.3.17

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if ( n % i == 0):
            # 약수임
            answer += i
    return answer
