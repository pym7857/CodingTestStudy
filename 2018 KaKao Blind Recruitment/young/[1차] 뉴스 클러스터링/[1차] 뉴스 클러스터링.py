import math
from collections import Counter

 

def solution(str1, str2):
    
    str1 = str1.upper()
    str2 = str2.upper()

    tmp = []
    tmp2 = []

    for i in range(0, len(str1)-1):
        if str1[i] == ' ' or str1[i+1] == ' ':
            continue
        if str1[i].isdigit() or str1[i+1].isdigit():
            continue
        if not(str1[i].isalpha()) or not(str1[i+1].isalpha()):
            continue

        tmp.append( str1[i] + str1[i+1] )        

    for i in range(0, len(str2)-1):
        if str2[i] == ' ' or str2[i+1] == ' ':
            continue
        if str2[i].isdigit() or str2[i+1].isdigit():
            continue
        if not(str2[i].isalpha()) or not(str2[i+1].isalpha()):
            continue

        tmp2.append( str2[i] + str2[i+1] )

        
    #print(tmp)
    #print(tmp2)


    if len(tmp) == 0 and len(tmp2) == 0: # 숫자나 공백, 특문때문에 전부 제거된 경우 예외처리 
        ans = 65536
        return ans
    else:
        c1 = Counter(tmp)
        c2 = Counter(tmp2)
        
        intersec = c1 & c2
        intersec = sum(list(intersec.values()))
        union = c1 | c2
        union = sum(list(union.values()))
        
        ans = intersec/union * 65536
    '''
        common = 0

        adding = 0

 

        tmp3 = tmp2

        # 두 리스트 공통 찾는 로직 ( set을 쓸 수가 없음 )

        for i in range(len(tmp)):
            for j in range(len(tmp3)):
                if tmp[i] == tmp3[j]:
                    common += 1
                    tmp3[j] == ''
                    break

 

        adding = len(tmp) + len(tmp2) - common

        

        a = common

        b = adding
        
        #print(common, adding)

        ans = a/b * 65536

        ans = math.floor(ans) # 내림 

    '''

    '''

        tmp = set(tmp)

        tmp2 = set(tmp2)

 

        print(tmp)

        print(tmp2)

 

        a = len(tmp & tmp2) # 교집합

        b = len(tmp | tmp2) # 합집합

        

        ans = a/b * 65536

    '''

    #print(int(ans))
    return int(ans)


#solution('FRANCE', 'french') 
#solution('handshake', 'shake hands')
#solution('aa1+aa2', 'AAAA12') 
#solution('E=M*C^2', 'e=m*c^2')
