from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 시작 위치 알아내기
sx, sy = 0, 0
for i in range(n):
    if board[i].count(2) > 0:
        sx = i
        sy = board[i].index(2)
        break

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[-1] * m for _ in range(n)] # 거리를 저장할 배열

def bfs(x, y):
    global visited
    queue = deque()
    visited[x][y] = 0
    queue.append([x, y, 0])

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and board[nx][ny] != 0: # 아직 방문하지 않았고 갈 수 있는 곳이면
                    visited[nx][ny] = d+1
                    queue.append([nx, ny, d+1])

bfs(sx, sy)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0: # 원래 못가는 곳이면 0출력
            print(0, end=' ')
        else: # 아니면 거리 출력
            print(visited[i][j], end=' ')
    print()