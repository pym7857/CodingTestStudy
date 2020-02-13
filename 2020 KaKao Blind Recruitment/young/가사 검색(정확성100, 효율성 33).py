import re

def solution(words, queries):
    res = [0]*len(queries)
    ans = []
    
    for idx, a in enumerate(queries):
        # 예외처리 (3가지 경우)
        if ( a.count('?') == 0 or (a[0] != '?' and a[-1] != '?'
                                                   and a.count('?') != 0) or
        (a.count('?') != len(a) and a[0] == '?' and
                                 a[-1] == '?') ):
            res[idx] = 0
            continue

        else:
            '''
            regex = re.compile("에러\s\d+")
            mc = regex.findall(a)
            print(mc)
            # 출력: ['에러 1122', '에러 1033']
            '''

            myindex = a.find('?')
            myindex_count = a.count('?')
            txt = a[:myindex]
            sign = a[myindex:]
            if a[0] != '?':  # '?' 가 처음 시작위치부터 있지 않을때 
                #print(a, txt, sign)
                compile_word = txt + '\w' + '{' + str(len(sign)) + '}'
                #print(compile_word)
            else:
                myindex += myindex_count
                #print(myindex)
                sign = a[:myindex] # ????
                txt = a[myindex:] # o
                #print(sign, txt)
                compile_word = '\w' +'{' + str(len(sign)) + '}' + txt
                #print(compile_word)
            

            final = []
            for b in words:
                if len(a) == len(b):
                    regex = re.compile(compile_word)
                    mc = regex.findall(b)
                    final.append(mc)
            #print('(a . final) = ', a, final)

            final = list(filter(None, final))
            #print(final)
            
            ans.append(len(final))

    #print(ans)
    return ans


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
