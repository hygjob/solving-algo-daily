# 2021.3.21
# 정수 내림차순으로 배치하기
# bubble sort 사용

def solution(n):
    answer = 0    
    sn = str(n)    
    arr = []
    for i in range(len(sn)):
        arr.append(int(sn[i]))
    
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    s = ''
    for i in range(len(arr)):
        s = s + str(arr[i])
        
    answer = int(s)
    
    return answer
