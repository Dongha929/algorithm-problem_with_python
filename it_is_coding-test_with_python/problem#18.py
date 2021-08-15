def alright(p):
    a = 0
    for i in p:
        if i == "(":
            a += 1
        else:
            a -= 1
        if a < 0:
            return False   
    return True

def split(p):
    a = 0
    for i in range(len(p)):
        if p[i] == '(':
            a += 1
        else:
            a -= 1
        if a == 0:
            return i
        
def solution(p):
    answer = ''
    if p == '':
        return answer
    i = split(p)
    u = p[:i + 1]
    v = p[i + 1:]
    if alright(u):
        answer =  u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        new = list(u[1:-1])
        # 문자열은 수정이 안된다
        for i in range(len(new)):
            if new[i] == '(':
                new[i] = ')'
            else:
                new[i] = '('
        # 리스트를 문자열로
        answer += "".join(new)
    return answer