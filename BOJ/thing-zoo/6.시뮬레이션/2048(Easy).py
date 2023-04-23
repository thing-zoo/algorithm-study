def rotate(board):
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = board[i][j]
    return rotated

def move(board): # 왼쪽방향에 대한 이동 함수
    moved = [[0]*n for _ in range(n)]
    for i in range(n):
        k = 0
        for j in range(n):
            if not board[i][j]: # 0은 건너뜀
                continue
            if moved[i][k] == 0: # 이동배열의 현재값이 없으면
                moved[i][k] = board[i][j] # 현재값 넣기
                continue
            if board[i][j] == moved[i][k]: # 값이 같으면
                moved[i][k] *= 2 # 더한값 넣고
                k += 1 # 다음 위치
            else: # 값이 다르면
                k += 1 # 다음 위치에
                moved[i][k] = board[i][j] # 현재값 넣기
            
    return moved

def dfs(k, board): #k: 이동횟수
    global answer
    if k == 5: # 최대 5번 이동했으면
        max_block = 0
        for i in range(n):
            for j in range(n):
                max_block = max(board[i][j], max_block)
        answer = max(max_block, answer)
        return # 종료
    # 좌
    dfs(k+1, move(board))
    # 하
    board = rotate(board)
    dfs(k+1, move(board))
    # 우
    board = rotate(board)
    dfs(k+1, move(board))
    # 상
    board = rotate(board)
    dfs(k+1, move(board))

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]
answer = 0
dfs(0, board)
print(answer)