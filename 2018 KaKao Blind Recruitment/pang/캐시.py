def solution(cacheSize, cities):
    time=0
    currentSize=0
    cache = []
    for i in cities:
        if i.lower() in cache: #있으면
            time+=1
            cache.remove(i.lower())#소문자로된거 제거
            cache.append(i.lower())#소문자로 된거 추가 -- 새로 추가함으로써 최근것으로
        else: # 없으면
            currentSize+=1
            time+=5
            if cacheSize != 0:# 캐시가 존재하면서
                if currentSize>cacheSize : #캐시가 차있을때만
                    currentSize-=1
                    cache.pop(0)   #최근껄 pop
                cache.append(i.lower())
    return time
