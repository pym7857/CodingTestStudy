
def solution(n, arr1, arr2):
    ans = [0]*n
    table1 = str.maketrans('1', '#')
    table2 = str.maketrans('0', ' ')
    for i in range(n):
        ans[i] = str(bin(arr1[i] | arr2[i]))[2:]
        while len(ans[i]) < n:
            ans[i] = '0' + ans[i]
        ans[i] = ans[i].translate(table1)
        ans[i] = ans[i].translate(table2)

    #print(ans)
    return ans

#solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
#solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
