def solution(N, stages):
    ans = []  
    fail = [0] * N # 해당 스테이지 실패인원
    all_num = len(stages) # 전체 시도한 사람 수 (전체 사람 수)

    for i in range(1,N+1): # 1,2,3,4,5
        num = stages.count(i) # 해당 스테이지에 머물러있는 사람
        if num == 0: # 예외처리 안해주면 '런타임 에러'
            fail_rate = 0
        else:
            fail_rate = num / all_num # 실패율

        # 튜플로 저장
        ans.append((i, fail_rate)) # tuple
        
        all_num -= num

    #print(ans)

    # 내림차순
    ans = sorted(ans, key=lambda t: t[1], reverse=True) # 튜플 내림차순 정렬
    #print(ans)
    ans = [i[0] for i in ans]
    #print(ans)
    return ans