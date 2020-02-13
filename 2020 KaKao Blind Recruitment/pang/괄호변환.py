def split(p):
    if p=='':
         return ''
    else:
        count=0
        for i,n in enumerate(p):
            if n==")":
                count-=1
            else:
                count+=1
            if count==0:
                break
        return p[:i+1],p[i+1:]

def checkTrue(u):
    count=0
    for i in u:
        if i=='(': #괄호가 열리면, 닫힌다.
            count+=1
        else:
            count-=1
        if count < 0:
            return False
    return True

def makeTrue(s):
    try:
        u,v=split(s)
    except:
        return ''
    answer=''
    if checkTrue(u):
        answer+=u
        answer+=makeTrue(v)
        return answer
    else:
        answer+='('
        answer+=makeTrue(v)
        answer+=')'
        u=u[1:-1]
        for i in u:
            if i=='(':
                answer+=')'
            else:
                answer+='('
        return answer
                
def solution(p):
    answer = makeTrue(p)
    return answer
