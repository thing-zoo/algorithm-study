import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 1
def updown():
    global board
    for i in range(n//2):
        for j in range(m):
            board[i][j], board[n-i-1][j] = board[n-i-1][j], board[i][j]

# 2
def leftright():
    global board
    for i in range(n):
        for j in range(m//2):
            board[i][j], board[i][m-j-1] = board[i][m-j-1], board[i][j]

# 3
def rotate_right(board):
    nboard = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            nboard[i][j] = board[n-j-1][i]
    return nboard

# 4
def rotate_left(board):
    nboard = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            nboard[i][j] = board[j][m-i-1]
    return nboard

# 5
def divide_right(board):
    nboard = [[0] * m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            nboard[i][m//2+j] = board[i][j]

    for i in range(n//2):
        for j in range(m//2, m):
            nboard[n//2+i][j] = board[i][j]
    
    for i in range(n//2, n):
        for j in range(m//2, m):
            nboard[i][j-m//2] = board[i][j]

    for i in range(n//2, n):
        for j in range(m//2):
            nboard[i-n//2][j] = board[i][j]
    return nboard

# 6
def divide_left(board):
    nboard = [[0] * m for _ in range(n)]
    
    # 1-> 4
    for i in range(n//2): # 1위치에 있는거
        for j in range(m//2):
            nboard[n//2+i][j] = board[i][j] 

    # 4-> 3
    for i in range(n//2, n):
        for j in range(m//2):
            nboard[i][m//2+j] = board[i][j]

    # 3-> 2
    for i in range(n//2, n):
        for j in range(m//2, m):
            nboard[i-n//2][j] = board[i][j]

    # 2->1
    for i in range(n//2):
        for j in range(m//2, m):
            nboard[i][j-m//2] = board[i][j]

    return nboard

cmd = list(map(int, input().split()))

for c in cmd:
    if c == 1:
        updown()
    elif c == 2:
        leftright()
    elif c == 3:
        board = rotate_right(board)
        n, m = m, n
    elif c == 4:
        board = rotate_left(board)
        n, m = m, n
    elif c == 5:
        board = divide_right(board)
    elif c == 6:
        board = divide_left(board)

for b in board:
    print(" ".join(map(str, b)))