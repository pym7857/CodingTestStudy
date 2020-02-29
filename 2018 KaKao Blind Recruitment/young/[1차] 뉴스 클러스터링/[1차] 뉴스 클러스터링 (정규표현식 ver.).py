import re
import math
from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    pattern = re.compile('[a-z][a-z]')

    tmp1 = []
    tmp2 = []

    for i in range(len(str1)-1):
        if pattern.search(str1[i:i+2]):
            tmp1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if pattern.search(str2[i:i+2]):
            tmp2.append(str2[i:i+2])
    #print(tmp1, tmp2)

    c1 = Counter(tmp1)
    c2 = Counter(tmp2)
    #print(c1, c2)

    intersection = c1 & c2
    union = c1 | c2

    a = sum(list(intersection.values()))
    b = sum(list(union.values()))

    if a == 0 and b == 0:
        return 65536
    
    ans = a / b * 65536
    ans = math.floor(ans)
    #print(int(ans))
    return int(ans)

#solution('FRANCE', 'french') 
#solution('handshake', 'shake hands')
#solution('aa1+aa2', 'AAAA12') 
#solution('E=M*C^2', 'e=m*c^2')
