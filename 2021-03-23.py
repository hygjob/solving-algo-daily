# 제일 작은 수 제거하기
# 2021.3.23
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]

    minv = min(arr)
    idx = arr.index(minv)

    del arr[idx]
    answer = arr
    return answer
