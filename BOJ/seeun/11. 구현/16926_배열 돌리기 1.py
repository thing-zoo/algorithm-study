import sys
input = sys.stdin.readline

n, m, r = map(int ,input().split())
board = [list(map(int ,input().split())) for _ in range(n)]

def rotate_left(t):
    global board

    tmp = board[t][t] # 테두리의 가장 왼쪽위에 있는 숫자 임시 저장

    # 상
    for j in range(t, m-1-t):
        board[t][j] = board[t][j+1]
    # 우
    for i in range(t, n-1-t):
        board[i][m-t-1] = board[i+1][m-t-1]
    # 하
    for j in range(m-t-1, t, -1):
        board[n-t-1][j] = board[n-t-1][j-1]
    # 좌
    for i in range(n-t-1, t, -1):
        board[i][t] = board[i-1][t]

    board[t+1][t] = tmp # 임시 저장한 수 옮기기


for t in range(min(n, m)//2): # 몇번째 테두리인지
    for _ in range(r%(((n-t*2)*2 + (m-t*2)*2 - 4))): # 나머지만큼만 돌리기
        rotate_left(t)


for i in range(n):
    print(" ".join(map(str, board[i])))