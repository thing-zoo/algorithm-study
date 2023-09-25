from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, t): # 구역 나누기 bfs
    global visited
    queue = deque()
    queue.append([x, y])
    board[x][y] = t
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < n and ny>=0:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    board[nx][ny] = t
                    visited[nx][ny] = True
                    queue.append([nx, ny])

def bfs2(t): # 다리 놓기 bfs
    global visited, dist, ans
    queue = deque()
    dist = [[-1]*n for _ in range(n)]

    # 현재 출발하는 섬의 위치를 모두 큐에 저장, dist 초기화
    for i in range(n):
        for j in range(n):
            if board[i][j] == t:
                dist[i][j] = 0
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < n and ny>=0:
                if board[nx][ny] and board[nx][ny] != t: # 출발한 땅이랑 다른 땅 만나면
                    ans = min(ans, dist[x][y])
                    return
                if board[nx][ny] == 0 and dist[nx][ny] == -1: # 바다이면 거리+1
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny]) 

# ---- 섬 카운트 -----
cnt = 1
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1

# ---- 다리 놓기 -----
ans = float('inf')
for i in range(1, cnt):
    bfs2(i)

print(ans)