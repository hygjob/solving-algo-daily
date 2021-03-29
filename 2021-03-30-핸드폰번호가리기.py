# 핸드폰번호가리기
# 2021.3.30
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    show_number = phone_number[-4:]
    #print(phone_number)
    #print(show_number)
    asterisk_number = '*' * (len(phone_number)-4)
    answer = asterisk_number + show_number
    return answer
