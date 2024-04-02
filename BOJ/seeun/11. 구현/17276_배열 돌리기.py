import sys
input = sys.stdin.readline
t = int(input())

def rotate_right(board):
    nboard = [board[i][:] for i in range(n)]

    # 주대각선 => 가운데 열
    for i in range(n):
        nboard[i][n//2] = board[i][i]

    # 가운데 열 -> 부대각선
    for i in range(n):
        nboard[i][n-i-1] = board[i][n//2]

    # 부대각선 -> 가운데 행
    for i in range(n):
        nboard[n//2][i] = board[n-i-1][i]
    # 가운데 행
    for i in range(n):
        nboard[i][i] = board[n//2][i]
    
    return nboard

def rotate_left(board):
    nboard = [board[i][:] for i in range(n)]
    # 주대각선 => 가운데 행
    for i in range(n):
        nboard[n//2][i] = board[i][i]

    # 가운데 열 -> 주대각선
    for i in range(n):
        nboard[i][i] = board[i][n//2]

    # 부대각선 -> 가운데 열
    for i in range(n):
        nboard[i][n//2] = board[i][n-i-1]

    # 가운데 행 -> 부대각선
    for i in range(n):
        nboard[n-i-1][i] = board[n//2][i]
    
    return nboard

for _ in range(t):
    n, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    if abs(d) == 0 or abs(d) == 360: # 0 or 360도 회전이면 그대로 출력
        board = board  
    elif d > 0: # 시계방향으로 d도 회전
        for r in range(d//45):
            board = rotate_right(board)
    elif d < 0: # 반시계방향으로 d도 회전
        for r in range(abs(d)//45):
            board = rotate_left(board)

    for i in range(n):
            print(" ".join(map(str, board[i])))