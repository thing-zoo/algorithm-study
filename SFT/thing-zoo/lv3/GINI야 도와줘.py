from collections import deque

def bfs():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    # 소나기의 각 위치별 도착시간 파악
    q = deque(rain)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] == 'X' or board[nx][ny] == 'H': # 강이나 태범이 집 확산 불가
                continue
            if dist_r[nx][ny] == float('inf'): # 방문안한 곳
                dist_r[nx][ny] = dist_r[x][y] + 1
                q.append([nx, ny])

    # 태범이의 각 위치별 도착시간 파악
    q = deque(taebeom)
    while q:
        x, y = q.popleft()
        if board[x][y] == 'H': # 집 도착
            return dist[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] == 'X': # 강 이동 불가
                continue
            if dist[x][y] + 1 >= dist_r[nx][ny]: # 소나기보다 빨리 도착하지 못하면
                continue
            if dist[nx][ny] == float('inf'): # 방문 안한 곳
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
    return 'FAIL'
        
r, c = map(int, input().split())
board = []
taebeom = [] # 태범이 초기위치
rain = []    # 소나기 초기위치
dist = [[float('inf')]*c for _ in range(r)]   # dist[i][j] = 태범이가 해당 위치에 도착한 시간
dist_r = [[float('inf')]*c for _ in range(r)] # dist_r[i][j] = 소나기가 해당 위치에 도착한 시간
for i in range(r):
    board.append(input())
    for j in range(c):
        if board[i][j] == 'W':
            taebeom.append([i, j])
            dist[i][j] = 0
        if board[i][j] == '*':
            rain.append([i, j]) # 소나기가 여러개일 수 있었다..!!!!! 테케 1,3,5,6 틀린 사람은 이것을 보십시오
            dist_r[i][j] = 0
print(bfs())