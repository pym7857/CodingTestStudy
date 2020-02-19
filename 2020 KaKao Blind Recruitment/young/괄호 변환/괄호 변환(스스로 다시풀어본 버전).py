def solution(p):
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == '':
        return ''

    # 문자열 w를 균형잡힌 괄호 문자열 u, v 로 분리
    (u, v) = split_str(p)
    #print( (u, v) )

    # 문자열 u가 올바른 괄호 문자열 이라면, 문자열 v에 대해 1단계부터 다시 시행
    if is_correct(u):
        u += solution(v)
        return u
    else: # 문자열 u가 올바른 괄호문자열이 아니라면,
        txt = '('
        txt += solution(v)
        txt += ')'
        u = u[1:-1]
        for idx, a in enumerate(u):
            if a == '(':
                u = u[:idx] + ')' + u[idx+1:]
            else:
                u = u[:idx] + '(' + u[idx+1:]
        txt += u
        return txt


# 균형잡힌 괄호문자열로 분리 ( '('와 ')'의 개수가 같은것 )
def split_str(p):
    c = 0
    idx = 0
    for i in range(len(p)):
        if p[i] == '(':
            c += 1
        else:
            c -= 1

        if c == 0:
           idx = i
           break
    return (p[:idx+1], p[idx+1:])

# 110001
# 올바른 괄호 문자열인지 판단 (짝이 모두 맞을경우)
def is_correct(u):
    #print(u)
    # u는 이미 균형잡힌 괄호 문자열
    # 열리면( '(' ) 닫혀야됨 ( ')' ) -> 스택 원리 이용 (리스트를 스택처럼)
    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

        #print(stack)

    if len(stack) == 0:
        return True
    else:
        return False

#print( solution("()))((()") )
#print( solution(")(") )
#print( solution("(()())()") )




