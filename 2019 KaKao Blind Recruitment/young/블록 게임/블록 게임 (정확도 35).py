#board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]

# 정답이 될 수 있는 블록은 총 5가지 유형. 
# 정답이 되는 블록이라 하더라도, 위를 막고있는 블록이 있나 검사 

# 5가지 유형의 블록인지 체크
def get_right_block(board, i, j):
    if (board[i][j] != 0 and i+1 < N and j+2 < N and board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i+1][j+2]):
        temp = []
        visited[i][j] = 1
        visited[i+1][j] = 1
        visited[i+1][j+1] = 1
        visited[i+1][j+2] = 1
        temp.append( [(i,j), (i+1,j), (i+1, j+1), (i+1, j+2)] )
        return ( (i, j+1), (i, j+2), temp ) # 나머지 공간의 검은색 두 부분을 리턴 
    
    elif (board[i][j] != 0 and i+2 < N and j-1 > 0 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+2][j-1]):
        temp = []
        visited[i][j] = 1
        visited[i+1][j] = 1
        visited[i+2][j] = 1
        visited[i+2][j-1] = 1
        temp.append( [(i,j), (i+1,j), (i+2, j), (i+2, j-1)] )
        return ( (i, j-1), (i+1, j-1), temp ) # 나머지 공간의 검은색 두 부분을 리턴 
    
    elif (board[i][j] != 0 and i+2 < N and j+1 < N and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+2][j+1]):
        temp = []
        visited[i][j] = 1
        visited[i+1][j] = 1
        visited[i+2][j] = 1
        visited[i+2][j+1] = 1
        temp.append( [(i,j), (i+1,j), (i+2, j), (i+2, j+1)] )
        return ( (i, j+1), (i+1, j+1), temp ) # 나머지 공간의 검은색 두 부분을 리턴 
    
    elif (board[i][j] != 0 and i+1 < N and j-2 > 0 and board[i][j] == board[i+1][j] == board[i+1][j-1] == board[i+1][j-2]):
        temp = []
        visited[i][j] = 1
        visited[i+1][j] = 1
        visited[i+1][j-1] = 1
        visited[i+1][j-2] = 1
        temp.append( [(i,j), (i+1,j), (i+1, j-1), (i+1, j-2)] )
        return ( (i, j-2), (i, j-1), temp ) # 나머지 공간의 검은색 두 부분을 리턴 
    
    elif (board[i][j] != 0 and i+1 < N and j-1 > 0 and j+1 < N and board[i][j] == board[i+1][j] == board[i+1][j-1] == board[i+1][j+1]):
        temp = []
        visited[i][j] = 1
        visited[i+1][j] = 1
        visited[i+1][j-1] = 1
        visited[i+1][j+1] = 1
        temp.append( [(i,j), (i+1,j), (i+1, j-1), (i+1, j+1)] )
        return ( (i, j-1), (i, j+1), temp ) # 나머지 공간의 검은색 두 부분을 리턴 

def is_loop_clean(board, q, w):
    for i in range(q):
        if board[i][w] != 0:
            return False
        
    return True

def remove_block(board, a, b, c, d, t):
    #print(t[0][0])
    for num in range(4):
        (i, j) = t[0][num]
        board[i][j] = 0    # 블록을 지움 
    
def solution(board):
    global visited, N
    N = len(board[0])
    visited = [[0]*N for i in range(N)]
    c2 = 0
    
    # 5가지 유형의 블록인지 검사 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if get_right_block(board, i, j) is not None:
                    ( (a,b), (c,d), t ) = get_right_block(board, i, j) 
                    #print(a,b,c,d)
                        
                    if ( is_loop_clean(board, a, b) and is_loop_clean(board, c, d) ):
                        #print(a,b,c,d)
                        c2 += 1
                        # 직사각형으로 꽉 채워지게 만들어진 블록은 이제 삭제
                        remove_block(board, a, b, c, d, t)
                        
                        #print(board)
                        
                
    #print(visited)
    
    return c2

#solution(board)