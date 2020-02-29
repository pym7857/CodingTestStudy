def solution(cacheSize, cities):
    if cacheSize == 0: # 예외처리 
        return 5* len(cities)

    for i in range(len(cities)): # 전부 소문자로 바꿔주기 
        cities[i] = cities[i].lower()
    
    start = 0
    end = cacheSize
    ans = 0
    
    while end < len(cities):
        tmp = cities[start:end]
        if cities[end] in tmp:
            ans += 1
        else:
            ans += 5
        start += 1
        end += 1
        #print(ans)

    ans += 5*cacheSize
    #print(ans)
    return ans
    
#solution(3, ['jeju', 'pangyo', 'seoul', 'jeju', 'pangyo', 'seoul', 'jeju', 'pangyo', 'seoul'] )
