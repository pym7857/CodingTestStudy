import re
import math

def regexp(str1):
    p = re.compile('[a-z][a-z]')
    result=[]
    for i in range(len(str1)):
        test=str1[i:i+2] # ? 질문: 미쳐버린 예외처리
        if p.search(test):
            result.append(test)
    return result

def solution(str1, str2):
    sub1=regexp(str1.lower())
    sub2=regexp(str2.lower())
    intersection=[]
    check=True
    while check is True:
        prevSub1=len(sub1)#시작전 길이
        for i in sub1:#교집합 ? 질문: 파이썬 루프 한번 더 반복하게 가능?
            if i in sub2:
                sub1.remove(i)
                sub2.remove(i)
                intersection.append(i)
        lenSub1=len(sub1)#시작후 길이
        if lenSub1==prevSub1: #같으면 더 안줄음 
            check=False
    union=len(sub1)+len(sub2)+len(intersection)
    try:
        answer = math.trunc(len(intersection)/union*65536)
    except ZeroDivisionError:
        answer =65536
    return answer
