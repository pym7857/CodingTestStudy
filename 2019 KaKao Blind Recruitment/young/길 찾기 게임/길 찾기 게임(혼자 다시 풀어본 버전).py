import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, x, idx):
        self.x = x
        self.idx = idx
        self.left = None
        self.right = None

preorder_list = []
postorder_list = []
    
def preorder(node):
    preorder_list.append(node.idx)
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)
    
def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    postorder_list.append(node.idx)
    
#nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    
def solution(nodeinfo):
    #print(len(nodeinfo))
    #print(nodeinfo[0])
    
    # 인덱스 붙히기 
    new_list = []
    for i in range(len(nodeinfo)):
        new_list.append( [nodeinfo[i], i+1] )
        
    #print(new_list)
    
    # y좌표 높은 순부터 정렬하기 
    new_list = sorted(new_list, key=lambda t: t[0][1], reverse=True)
    print(new_list)
    
    # 루트 지정
    root = Node(new_list[0][0][0], new_list[0][1])
    
    for i in range(1, len(new_list)): # 1~8번째 노드까지 해당 (root노드 제외)
        parent = root # 단순 값을 빌려가는게 아니고, Node Class 참조를 빌려가는 것
        
        while(True):
            if parent.x < new_list[i][0][0]:
                if parent.right is None:
                    parent.right = Node(new_list[i][0][0], new_list[i][1])
                    break
                else:
                    parent = parent.right
            else:
                if parent.left is None:
                    parent.left = Node(new_list[i][0][0], new_list[i][1])
                    break
                else:
                    parent = parent.left
    
    preorder(root)
    postorder(root)
    
    return [preorder_list, postorder_list]

#solution(nodeinfo)

#print(preorder_list)
#print(postorder_list)