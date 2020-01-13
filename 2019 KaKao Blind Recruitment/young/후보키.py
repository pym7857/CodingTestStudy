from itertools import chain, combinations

# 모든 부분집합을 구하는 함수 (stackOverflow 참조)
def get_all_subset(iterable): # 매개변수 : 리스트
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# 후보키: 1.유일성  2.최소성
    
# 위 부분집합 중에서 1.유일성을 만족하는 부분집합을 구하는 함수
def get_all_unique_subset(relation): # 중복되는게 있는지 확인하는 함수
    subset_list = get_all_subset(list(range(len(relation[0])))) # [0,1,2,3] 의 모든 부분집합 -> 열의 이름을 0,1,2,3...등 으로 바꾼것
    unique_list = []
    
    # 유일성을 만족하는지 체크
    for subset in subset_list:    # [0],[1],[0,1],[0,1,2] .. (= 학번, (학번,이름)... )
        unique = True
        row_set = set()      # 하나의 부분집합의 모든행에 대한 row 저장소

        # 모든행을 돌면서 중복되는 행(문자열)이 있는지 확인
        for i in range(len(relation)):     # i = 0,1,2,3,4,5..
            row = ' '
            for j in subset:
                row += relation[i][j] + '.'	# 100.ryan등으로 바꿈
            if row in row_set:
                unique = False
                break 		# 모든 행을 도는 for문 즉시 빠져나감 
            row_set.add(row)

        # 유일성을 만족하는 부분집합에 대해서만..
        if unique == True:
            unique_list.append(subset)
            
    return unique_list

# 위 부분집합 중에서 2.최소성을 만족하는 부분집합을 구하는 함수 
def solution(relation):
    unique_list = get_all_unique_subset(relation)
    unique_list = sorted(unique_list, key=lambda t:len(t))  # 부분집합의 크기가 작은 순서대로 정렬 ->   ex) [1], [1,2] ...
    
    answer_list = []
    
    # 최소성을 만족하는지 체크
    for subset in unique_list: 	 # subset = [1], [1,2] ...
        check = True
        for j in answer_list:
            if j.issubset(subset):	 # 크기가 작은 부분집합이, 크기가 큰 부분집합의 부분집합인지 체크
                check = False
        if check == True:
            answer_list.append(subset)
    
    return len(answer_list)