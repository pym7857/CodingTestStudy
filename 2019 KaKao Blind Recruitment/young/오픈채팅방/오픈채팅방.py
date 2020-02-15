def solution(record):
    ans = []

    #record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    # Key,Value - > uid, 닉네임
    user_list = {} # dict

    #print(record[0])

    for v in record:
        v_list = v.split(' ')
        #print(v_list)
        if v_list[0] == 'Enter' or v_list[0] == 'Change':
            user_list[v_list[1]] = v_list[2]

    #print(user_list) # 최종 닉네임 출력


    # 최종 출력 
    for v in record:
        v_list = v.split(' ')
        #print(v_list)
        if v_list[0] == 'Enter':
            ans.append(user_list[v_list[1]]+'님이 들어왔습니다.')
        elif v_list[0] == 'Leave' :
            ans.append(user_list[v_list[1]]+'님이 나갔습니다.')

    return ans