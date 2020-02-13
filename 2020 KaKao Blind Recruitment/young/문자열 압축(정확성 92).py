


def solution(s):
    if len(s) == 1:
        return 1
    
    length = len(s)
    #print(length)
    l = length // 2 # [0,1,2,3,4]   5 // 2 =  2. => 0, 1 까지 자르는것만 의미o

    min_value = 1001 
    for i in range(1, l+1): # i = 1, 2 (1개씩 자름, 2개씩 자름)
        lst = []
        start = 0
        end = i

        flag = 0
        c = 0 # 마지막에 더해야할 숫자 
        final_str = ''
        
        while True:
            lst.append( s[start:end] )
            start = end
            end += i

            if end > length:
                lst.append(s[start:length])
                break
        #print(lst)

        '''
        for a, b in zip(lst, lst[1:]):
            print(a, b)
            if a == b:
                
                flag = 1 # 같은게 나오면 깃발꽂음 
            else:
                if flag == 1: # 같은게 나오다가 다른게 나왔을때
                    c += 1 
                    flag = 0
                #else: # 다른게 계속 나왔을때 
        '''
        flag = 0
        seq = 0 # 연속되는 숫자의 개수 
        
        for k in range(len(lst)-1):
            if lst[k] == lst[k+1]: # 같은게 나오면
                flag = 1
                seq += 1
                lst[k] = '' # 이전 문자 공백으로 만듦 
            else: # 다른게 나오면
                if flag == 1: # 앞에꺼가 같은 문자 였다면 
                    c += 1
                    
                    seq += 1
                    if seq >= 10: # 10cde
                        c += 1
                        if seq >= 100: # 100cde
                            c += 1
                            if seq >= 1000: # 1000cde
                                c += 1
                    flag = 0
                    seq = 0
                else:
                    continue
        #print('(i, c, lst) = ', i, c, lst)
        final_state = ''
        for a in lst:
            if a != '':
                final_state += a
        #print('final_state = ', final_state)
        
        if c >= 10:
            c += 1
            if c >= 100:
                c += 1
                if c >= 1000:
                    c += 1

        final_len = len(final_state) + c
        #print('final_len = ', final_len)
        
        if final_len < min_value :
            min_value = final_len

    return min_value


#print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxd"))
