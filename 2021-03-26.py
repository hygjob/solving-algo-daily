# 최대공약수와 최소공배수
# 2021.3.26
# https://programmers.co.kr/learn/courses/30/lessons/12940

# 최대공약수
def gcd(x , y):
    while y:
        x, y = y, x % y
    return x

# 최소공배수
def lcm(x, y):
    return x * y // gcd(x, y)

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    
    return answer
