# target number
# https://programmers.co.kr/learn/courses/30/lessons/43165
def dfs( prev, index, numbers, target):

    if index >= len(numbers):
        if target == prev:

            return 1
        return 0
    cur1 = prev + numbers[index]
    cur2 = prev - numbers[index]

    ans = 0
    ans += dfs(cur1, index+1, numbers, target)
    ans += dfs(cur2, index+1, numbers, target)

    return ans


def solution(numbers, target):
    answer = 0
    current = numbers[0]
    answer += dfs(current, 1, numbers, target)
    answer += dfs(-current, 1, numbers, target)
    return answer
