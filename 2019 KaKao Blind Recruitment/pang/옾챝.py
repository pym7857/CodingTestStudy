def solution(record):
    answer = []
    userDictionary={}
    
    #유저 딕셔너리 생성
    for input in record:
        input = input.split()
        if input[0] in ['Enter','Change']:
            userDictionary[input[1]]=input[2]
    #문자열 생성        
    for input in record:
        input = input.split()
        test=userDictionary[input[1]]
        if input[0] in ['Enter']:
            test +='님이 들어왔습니다.'
        elif input[0] in ['Leave']:
            test +='님이 나갔습니다.'
        else:
            continue
        answer.append(test)
                     
    return answer
