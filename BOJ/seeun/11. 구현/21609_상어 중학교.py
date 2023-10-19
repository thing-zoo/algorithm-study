from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate_right(before):
    after = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            after[j][N-i-1] = before[i][j]

    return after

def rotate_left(before):
    after = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            after[N-j-1][i] = before[i][j]

    return after

def push_left(before):
    after = [[-2] * N for _ in range(N)]
    for i in range(N):
        idx = 0
        black = False
        for j in range(N):
            if not black and before[i][j] > -1: # 자연수이거나 무지개면
                after[i][idx] = before[i][j]
                idx += 1
            elif board[i][j] == -1:
                idx = j
                after[i][idx] = -1
                idx += 1
    return after

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(gx, gy): # 블록 크기와 무지개 개수 구하기
    global visited
    cnt, rainbow = 1, 0
    color = board[gx][gy]
    queue = deque()
    visited[gx][gy] = True
    queue.append([gx, gy])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and (board[nx][ny] == color or board[nx][ny] == 0): # 같은 색이거나 무지개색이면
                    visited[nx][ny] = True
                    cnt += 1
                    if board[nx][ny] == 0:
                        rainbow += 1
                    queue.append([nx, ny])

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                visited[i][j] = False

    return cnt, rainbow, gx, gy

def remove_bfs(x, y, board): # 블록 그룹 없애기
    visited = [[False] * N for _ in range(N)]
    board = [board[i][:] for i in range(N)]
    
    color = board[x][y]
    queue = deque()
    visited[x][y] = True
    queue.append([x, y])
    board[x][y] = -2
    

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and (board[nx][ny] == color or board[nx][ny] == 0): # 같은 색이거나 무지개색이면
                    visited[nx][ny] = True
                    board[nx][ny] = -2 # 없애기
                    queue.append([nx, ny])
    return  board

score = 0
temp = 0

while True:
    visited = [[False] * N for _ in range(N)]
    candi = []

    # 가장 큰 블록 그룹 구하기
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0: # 일반색이고 아직 방문하지 않았으면
                tmp = bfs(i, j)
                if tmp[0] > 1: # 블록 그룹이면
                    candi.append(tmp) # 후보에 넣음

    # 문제의 조건에 따라 정렬 후 가장 앞에 있는 값 사용
    candi.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))

    # 블록 그룹이 하나도 없으면 종료
    group = 0
    for c in candi:
        if c[0] >= 2:
            group += 1
    if group == 0:
        break
    
    # 점수 계산, 블록 제거
    score += (candi[0][0]**2) # 블록개수 제곱만큼 점수 더함
    board = remove_bfs(candi[0][2], candi[0][3], board)
    
    # 중력작용
    board = rotate_right(board)
    board = push_left(board)
    board = rotate_left(board)

    # 반시계 90도 회전
    board = rotate_left(board)
 
    # 중력작용
    board = rotate_right(board)
    board = push_left(board)
    board = rotate_left(board)

print(score)