def solution(n, arr1, arr2):
    answer = conv2map(n,arr1,arr2)
    return answer

def conv2map(n,arr1,arr2):
    convMap = []
    for i in range(n):
        temp=""
        bin1=bin(arr1[i])[2:].zfill(n)
        bin2=bin(arr2[i])[2:].zfill(n)
        #bin3=bin(arr1|arr2).zfill(n)
        for j in range(n):
            if (bin1[j]=="1") or (bin2[j]=="1"):
                temp+="#"
            else:
                temp+=" "
        convMap.append(temp)
    return convMap
