from collections import deque
EMPTY = -2
BLACK = -1
RAINBOW = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
def find_block_group(a, b):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    rainbow = []
    normal = []
    normal.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if not visited[nx][ny]: # 방문 안한 곳
                if board[nx][ny] == RAINBOW: # 무지개거나
                    rainbow.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[normal[0][0]][normal[0][1]] == board[nx][ny]: # 같은색이거나
                    normal.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))

    for x, y in rainbow:  # 무지개블록은 얼마나 있든 상관없으므로
        visited[x][y] = False  # 다시 포함될 수 있음..

    return (len(normal)+len(rainbow), len(rainbow), normal + rainbow) # 크기, 무지개 개수, 블록

def remove_block_group(group):
    for x, y in group:
        board[x][y] = EMPTY

def gravity():
    for j in range(n):
        temp = [EMPTY]*n
        for i in range(n):
            if board[i][j] == BLACK:
                temp[i] = BLACK
        k = n-1
        for i in range(n-1, -1, -1):
            if board[i][j] == EMPTY: continue
            if board[i][j] == BLACK:
                k = i-1
                continue
            if temp[k] == EMPTY:
                temp[k] = board[i][j]
                k -= 1
        for i in range(n):
            board[i][j] = temp[i]
def rotate():
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[n-j-1][i] = board[i][j]
    return rotated

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    block_groups = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > RAINBOW: # 일반블록이면서 방문 안한 곳
                block_group = find_block_group(i, j)
                if block_group[0] >= 2: # 크기가 2이상이여야함
                    block_groups.append(block_group)
    block_groups.sort(reverse=True)
    if not block_groups: break # 블록이 없으면 종료
    remove_block_group(block_groups[0][2])
    answer += block_groups[0][0]**2
    gravity()
    board = rotate()
    gravity()
print(answer)