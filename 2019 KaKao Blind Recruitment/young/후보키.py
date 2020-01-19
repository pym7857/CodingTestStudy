from itertools import chain, combinations

# 모든 부분집합을 구하는 함수 (stackOverflow 참조)
def get_all_subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))   # 집합형태가 아닌, 튜플 형태로 반환 

# 1. 유일성을 만족하는 집합 구하기 
def get_all_uniq_subset(relation):
    # 모든 column의 이름을 0, 1, 2, 3 으로 표현 
    subset_list = get_all_subset(list(range(len(relation[0])))) # list(range(len(relation[0]))) = [0, 1, ,2, 3]
                                                                # subset_list = (0,), (1), .. (0,1), ...(0,1,2,3)
    uniq_list = []
    
    col_count = len(relation[0]) # 열의 개수 = 4
    row_count = len(relation) # 행의 개수 = 6
    
    # 부분집합 하나하나에 대해서, 
    for subset in subset_list: # subset_list = (0,), (1), .. (0,1), ...(0,1,2,3)
        uniq = True
        row_set = set() # 어떠한 부분집합의 모든 행에 대한 값 저장소
    
        for i in range(row_count): # 모든 행을 돌면서 유일성을 만족하는지 검사 
            row = ' '  # 행 문자열 담을 공간
            for j in subset: 
                row += relation[i][j] + '.'  # 튜플을 100.ryan. 등의 문자열로 저장 
                
            if row in row_set:
                uniq = False
                break
            else:
                row_set.add(row) # 한 행 마다 row_set에 추가 
    
        # 하나의 부분집합에 대해서 모든 행을 돌고난뒤
        if uniq == True:
            uniq_list.append(subset)
    
    return uniq_list
    
# 2. 최소성을 만족하는 집합 구하기 
# 유일성을 만족하는 부분집합에 속하는 부분집합들을 걸러주면 된다.
def solution(relation):
    uniq_list = get_all_uniq_subset(relation)
    uniq_list = sorted(uniq_list, key=lambda t:len(t)) # 길이순으로 오름차순 정렬 
    # print(uniq_list)

    answer_list = [] # 중복이 없는 집합들의 집합 (길이가 짧은 집합부터 들어간다)
    
    # 최소성을 만족하는지 체크
    for uniq in uniq_list: # uniq_list = [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
        uniq = set(uniq) # 튜플 -> 집합 형태로 변환 (issubset함수 사용 가능)
        check = True
        
        for j in answer_list:
            if j.issubset(uniq): # 길이가 짧은 answer_list 집합의 원소가, uniq에 속하는지 체크 
                check = False
        
        if check == True:
            answer_list.append(uniq)
        
        
    return len(answer_list)
    
# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])