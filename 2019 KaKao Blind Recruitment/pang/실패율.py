def solution(N, stages):
    failList = []
    answer = []
    #실패율 도달했지만, 클리어 x / 도달한 사람은 스테이지보다 숫자가 큰사람
    # 1실패율 1/8 2실패율 3/7 3실패율 2/4 4실패율 1/2 5실패율0
    for i in range(1,N+1):
        failure=0
        arrivedUser=0
        notClearUser=0
        for j in range(0,len(stages)):
            if stages[j]==i:
                notClearUser+=1
            if stages[j]>=i:
                arrivedUser+=1     
        if arrivedUser==0:
            failure=0
        else:
            failure=notClearUser/arrivedUser
        failList.append(failure) 
    
    for i in range(0,N):
        index=0
        key=-1
        for j in range(0,N):
            if failList[j]>key:
                key=failList[j]
                index=j
        failList[index]=-1
        answer.append(index+1)
                    
    return answer
    
   ## return sorted(result, key=lambda x : result[x], reverse=True) 이거 
