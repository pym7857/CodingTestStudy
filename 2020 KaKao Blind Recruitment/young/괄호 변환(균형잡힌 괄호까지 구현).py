import sys

def right(u):
    div = len(u) // 2
    org = u[:div]
    rev = u[div:]
    rev_r = rev[::-1]
    if decal(org, rev_r, div):
        return True
    else:
        return False

def decal(a, b, l):
    #print(a, b, l)
    for i in range(l):
        if (a[i] == '(' and  b[i] == '(') or (a[i] == ')' and  b[i] == ')'):
            return  False
    return True

def split_balance(p):
    s = 0
    for i in range(len(p)):
        if p[i] == '(':
            s += 1
        else:
            s -= 1

        div = i // 2
        org = p[:div+1]
        rev = p[div+1:i+1]
        rev_r = rev[::-1]
        
        #print(i, org, rev, s, rev_r)
        if i%2 !=0 and s == 0:
            if decal(org, rev_r, div+1):
                return (p[:i+1], p[i+1:])             

def solution(p):
    if p == '':
        return ''

    num = 0

    # 균형잡힌 괄호 문자열 (짝수, 합해서0, 데칼코마니 )
    (u, v) = split_balance(p)
    print(u, v)

    if num == 0:
        if (right(u)): # u가 올바른 괄호 문자열 이라면..
            solution(v)
            num += 1
        else: # u가 올바른 괄호 문자열이 아니라면 
            new = '('
    else:
        # 포기 
        
        
        


solution("(()())()")
