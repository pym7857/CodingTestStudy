# 하나하나 디버깅 해가면서 풀이 

import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, x, id, left_bound, right_bound): # Node(x좌표, id, 왼쪽bound, 오른쪽bound)
        self.x = x 
        self.id = id   # 노드 번호 (1,2,3...)
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left_node = None
        self.right_node = None

preorder_result = []
postorder_result = []

def preorder(node):
    preorder_result.append(node.id)
    if node.left_node is not None:
        preorder(node.left_node)
    if node.right_node is not None:
        preorder(node.right_node)

def postorder(node):
    if node.left_node is not None:
        postorder(node.left_node)
    if node.right_node is not None:
        postorder(node.right_node)
    postorder_result.append(node.id)
    
def solution(nodeinfo): # nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    nodeinfo = [i + [idx + 1] for idx, i in enumerate(nodeinfo)] # idx, i = 0, [5, 3]
                                                                  # idx, i = 1, [11, 5]
    # nodeinfo = [5, 3, 1] -> 각 노드에 1,2,3...등 번호를 부여
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True) # y 좌표 기준으로 내림차순 정렬
    # print(nodeinfo)
    # 현재 nodeinfo = [[8, 6, 7], [11, 5, 2], [3, 5, 4], [5, 3, 1], [13, 3, 3], [1, 3, 6], [7, 2, 8], [2, 2, 9], [6, 1, 5]]
    
    array = [] # 같은 y좌표에 여러개의 x 좌표가 들어가도록 리스트 구성
    now = -1
    
    # array : 각 레벨(level)별로 원소들이 담긴 리스트 새로 구성
    for i in nodeinfo:
        y = i[1] # nodeinfo의 두번째원소(=y좌표)
        if y != now:
            array.append([]) # 공간 만듦 
            now = y
        array[len(array) - 1].append((i[0], i[2])) 
        # print(array)
        # 현재 array = [[(8, 7)], [(11, 2), (3, 4)], [(5, 1), (13, 3), (1, 6)], [(7, 8), (2, 9)], [(6, 5)]]
    for i in range(len(array)):
        array[i] = sorted(array[i]) # array의 각 원소 오름차순 정렬
    
    # print(array)
    # 현재 array = [[(8, 7)], [(3, 4), (11, 2)], [(1, 6), (5, 1), (13, 3)], [(2, 9), (7, 8)], [(6, 5)]]
    # 이제, 레벨별로 해당 원소들이 담기는것 까지 완성
    
    root = Node(array[0][0][0], array[0][0][1], 0, 100000) # 루트 노드 설정 = (8, 7)노드 (여기서 노드는 '객체')
                                                           # 0~100,000은 문제에 나와있는 x범위
    
    node_list = [[]]
    node_list[0].append(root)
    for level in range(1, len(array)): # root레벨은 제외한, 두번째 level부터 차례대로 확인
        node_list.append([]) # 이번 레벨에 해당하는 노드 담을 공간 만듦 
        for data in array[level]: # array[1] = [(3,4), (11,2)]     data = (3, 4), (11, 2)
            x = data[0]    # x = 3
            id = data[1]   # id = 4
            for parent_node in node_list[level - 1]: # level-1은 부모노드
                # 현재 parent_node = (8, 7)
                if parent_node.left_bound <= x and parent_node.x > x: # 부모의 왼쪽자식이 되는경우
                    now_node = Node(x, id, parent_node.left_bound, parent_node.x) # parent노드의 left_bound를 그대로 가지고 right_bound는 parent노드의 x좌표가 됨
                    parent_node.left_node = now_node # 부모의 왼쪽자식으로 붙힘 
                    node_list[level].append(now_node)
                    break
                elif parent_node.right_bound >= x and parent_node.x < x: # 부모의 오른쪽자식이 되는경우
                    now_node = Node(x, id, parent_node.x, parent_node.right_bound) # left_bound는 parent노드의 x좌표가 되고, parent노드의 right_bound를 그대로 갖음
                    parent_node.right_node = now_node
                    node_list[level].append(now_node)
                    break
    preorder(root)
    postorder(root)
    return [preorder_result, postorder_result]

# 정답 확인
# solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])