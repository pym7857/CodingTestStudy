'''
저도 동일한 점수가 나와서 질문을 좀 참고해 봤는데, LRU에 대한 자세한 지식이 부족해서 그랬던 것 같습니다.
Cash Hit 상태에서 다음에 지워질 Key가 바뀔 수 있습니다.
가령 현재 캐시에 남아있는 키 중 서울이 가장 오래 전에 사용되었더라도 서울을 검색한다면
가장 최근에 사용한 것으로 수정해야 합니다.
따라서 캐시 히트 상태에서 캐시에 저장된 키들의 순서를 바꿔주는 코드가 필요합니다.
'''

def solution(cacheSize, cities):
    cities = [i.lower() for i in cities] # 소문자로 
    answer = 5
    cache = [cities[0]]
    
    if cacheSize == 0: # 예외처리 
        answer += 5 * (len(cities) -1)
    else:
        for i in cities[1:]:
            if len(cache) < cacheSize and i in cache: # 아직 cache배열이 cacheSize만큼 채워지지 않은 경우 + hit인 경우
                cache.pop(cache.index(i))
                answer += 1
            elif len(cache) < cacheSize: # 아직 cache배열이 cacheSize만큼 채워지지 않은 경우 + miss인 경우 (빼내지 않고 그냥 삽입한다.)
                answer += 5
            elif i in cache: # hit인 경우 
                cache.pop(cache.index(i))
                answer += 1
            else:
                del cache[0] # miss 됐을경우 가장 앞의 것을 꺼낸다.
                answer += 5
            cache.append(i)
    return answer
