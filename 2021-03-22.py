# 2021.3.22
# 정수 제곱근 판별
import math

def solution(n):
    answer = 0
    nsqrt = int(math.sqrt(n))
    if (nsqrt**2 == n):
        answer = (nsqrt +1)**2
    else:
        answer = -1

    return answer
