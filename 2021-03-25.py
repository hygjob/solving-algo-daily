# 키패드 누르기
# 2021.3.25
# https://programmers.co.kr/learn/courses/30/lessons/67256
    
pads = {'1': (1,1), '2':(1,2), '3':(1,3),
       '4':(2,1), '5':(2,2), '6':(2,3),
       '7':(3,1), '8':(3,2), '9':(3,3),
       '*':(4,1), '0':(4,2), '#':(4,3)}

# 보다 짧은 거리
def shorter(cl, cr, num, hand):
    clp = pads[str(cl)]
    crp = pads[str(cr)]
    nump = pads[str(num)]
    dist_from_left = abs(clp[0] - nump[0]) + abs(clp[1] - nump[1])
    dist_from_right = abs(crp[0] - nump[0]) + abs(crp[1] - nump[1])
    if dist_from_left < dist_from_right:
        return 'L'
    if dist_from_left > dist_from_right:
        return 'R'
    if dist_from_left == dist_from_right:
        if hand == 'left':
            return 'L'
        else:
            return 'R'
    return ''
    
    
# 답구하기
def solution(numbers, hand):
    answer = ''
    cl = '*'
    cr = '#'
    
    for i in range(len(numbers)):
        curv = numbers[i]
        if curv in (1,4,7):
            answer += 'L'
            cl = str(curv)
        if curv in (3,6,9):
            answer += 'R'
            cr = str(curv)
        if curv in (2,5,8,0):
            val = shorter(cl, cr, curv, hand)
            answer += val
            if (val == 'L'):
                cl = str(curv)
            else:
                cr = str(curv)
    return answer

if __name__ == '__main__':
    answer = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
    print(answer)
    answer = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')
    print(answer)
    answer = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')
    print(answer)
