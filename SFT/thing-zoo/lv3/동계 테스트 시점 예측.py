from collections import deque

def bfs():
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if not visited[nx][ny] and board[nx][ny] == 0: # 방문안한 외부 공기면
                q.append((nx, ny)) # 넣고
            if board[nx][ny]: # 얼음이면
                board[nx][ny] += 1 # 외부공기와 만날때마다 카운트
            visited[nx][ny] = True

def melt():
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 3: # 외부공기랑 2번이상 만났으면
                board[i][j] = 0 # 녹이기
                count += 1
            elif board[i][j] == 2:
                board[i][j] = 1
    return count

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 초기 얼음 개수 세기
total_ice = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            total_ice += 1

answer = 0
while total_ice > 0:
    bfs()
    total_ice -= melt()
    answer += 1
print(answer)