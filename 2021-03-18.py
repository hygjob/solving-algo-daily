# 2021.3.19
# 자릿수 더하기

def solution(n):
    answer = 0


    s = str(n)
    for i in range(0, len(s)):
        answer += (int)(s[i])
    

    return answer
