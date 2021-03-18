# 이상한 문자 만들기
# 2021.3.18

def solution(s):
    answer = ''
    words = s.split(' ')
    for i in range(0, len(words)):
        word = words[i]
        cword = ''
        for j in range(0, len(word)):
            if (j %2 == 0):
                
                cword += word[j].upper()                
            else :
                cword += word[j].lower()
        answer += cword + ' '
    alength = len(answer)
    answer = answer[0:alength-1]
    return answer
