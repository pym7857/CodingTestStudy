# for문 돌면 시간초과
# 시간이 적게 걸리는 음식부터 확인하는 그리디 알고리즘 으로 문제를 푼다

from queue import PriorityQueue

def solution(food_times, k):
    if sum(food_times) <= k: # 먹을 음식의 (종류)개수보다 k가 크다면 
        return -1
    
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1)) # 튜플(음식의 시간, index)
        
    # q = ( (8, 1), (6, 2), (4, 3) ) ... (x)
    # 우선순위큐는 튜플의 첫번째 원소를 기준으로 '자동으로' 오름차순 됨
    # -> 음식의 시간을 기준으로 오름차순 됨
    # q = ( (4, 3), (6, 2), (8, 1) ) ... (o)
    
    # print(q.queue[0][0])   # 4
    
    prev = 0
    num = len(food_times) # 음식의 (종류)개수
    
    # 빼야될 값이 k보다 작은 경우에만 while문 실행
    while (q.queue[0][0] - prev) * num <= k:
        now = q.get()[0] # 원소 가져옴
        k -= (now - prev) * num
        
        num -= 1
        prev = now
        
        
    # while문 빠져나와서.. (남아있는 시간보다 뺄 시간이 더 큰 경우)
    # 남아있는 튜플들을 index 오름차순으로 일렬로 나열한다

    arr = sorted(q.queue, key=lambda x: x[1]) # index 순으로 오름차순 정렬 
    # arr = ( (8, 1), (6, 2) )
    
    # print (k) # k = 3
    
    quote = k // num
    remainder = k - quote * num
        
    # print(quote)
    # print(remainder)
    return arr[remainder][1]
    
# solution([8,6,4], 15)