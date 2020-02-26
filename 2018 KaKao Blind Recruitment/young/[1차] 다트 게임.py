def solution(res):
    #temp = ['']*3
    ans = [0]*3
    i = 0
    flag = 1
    for a in res:
        if a.isdigit():
            if flag == 1:
                ans[i] = int(a)
            else:
                ans[i] = 10
            flag = 0
        else:
            flag = 1
            if a.isalpha():
                ans[i] = int(ans[i])
                if a == 'S':
                    ans[i] **= 1
                elif a== 'D':
                    ans[i] **= 2
                else:
                    ans[i] **= 3
                i += 1
                    
            else:
                if a == '#':
                    ans[i-1] *= -1
                else:
                    if i >= 2:
                        ans[i-1] *= 2
                        ans[i-2] *= 2
                    else:
                        ans[i-1] *= 2
        #print(i, ans)

    print(sum(ans))

solution('1D2S3T*')

