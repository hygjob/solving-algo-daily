dict_upper = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

reversed_dict_upper = dict(map(reversed, dict_upper.items()))


dict_lower = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

reversed_dict_lower = dict(map(reversed, dict_lower.items()))


dict_space = {' ': 1}


def findpos(l):

    if l.isupper() == True:    
        r = dict_upper[l]
        return 'UPPER', r
    
    if l.islower() == True:
        r = dict_lower[l]    
        return 'LOWER', r
    
    return 'SPACE', 1
    
def caesar(letter, n):
    ty, r = findpos(letter)
    if ty == 'UPPER':
        new_pos = (r-1 + n ) % 26 + 1
        res = reversed_dict_upper[new_pos]
    
    if ty == 'LOWER':
        new_pos = (r-1 + n ) % 26 + 1
        res = reversed_dict_lower[new_pos]
        
    if ty == 'SPACE':
        new_pos = 1
        res = ' '
    
    return res

def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        answer += caesar(s[i], n)
    return answer
