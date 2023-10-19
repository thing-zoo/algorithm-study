from collections import deque
N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
step = list(map(int, input().split()))

def rotate(board, x, y, length): # 움직여야하는 격자만 회전시킴
    new_board = [[0]*length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            new_board[j][length-i-1] = board[x+i][y+j]
    return new_board

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def melt():
    n = 2**N
    new_board = [[0]*n for _ in range(n)] # 녹은 후의 상태를 저장

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue
            cnt = 0
            for i in range(4): # 상하좌우
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] > 0: # 얼음 있으면 카운트
                    cnt += 1

            if cnt < 3: # 주변에 얼음이 3개 미만이면 현재 위치 얼음 녹음
                new_board[x][y] = board[x][y] - 1
            else:
                new_board[x][y] = board[x][y]

    return new_board

# 회전 규칙 주어진 만큼 반복
for s in step:
    n = 2**N
    for i in range(0, n, 2**s):
        for j in range(0, n, 2**s):
            rotated = rotate(board, i, j, 2**s)

            for k in range(2**s):
                board[i+k][j:j+2**s] = rotated[k][:]
    board = melt()

def bfs(x, y): # bfs로 얼음 구역 크기 측정
    global visited
    n = 2**N
    cnt = 1 # 현재 덩어리의 얼음 개수
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1 # 현재 덩어리에 포함된 얼음 개수 +1
    return cnt

visited = [[False]*(2**N) for _ in range(2**N)]
maxplace = 0
total = 0
for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and board[i][j] > 0:
            tmp = bfs(i, j) # 얼음 덩어리 크기
            maxplace = max(maxplace, tmp) # 최대 덩어리 갱신
        total += board[i][j]

print(total)
print(maxplace)
