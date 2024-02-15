from collections import deque
n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

knife = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            knife = [i, j]
            break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, xx, yy): # 출발지 x, y 도착지 xx, yy
    ans = float('inf')
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    queue.append([x, y, 0])
    while queue:
        x, y, dist = queue.popleft()
        if x == xx and y == yy: # 목적지에 도착했으면
            ans = min(ans, dist)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] != 1: # 벽이 아니면 통과
                    visited[nx][ny] = True
                    queue.append([nx, ny, dist + 1])
    return ans

res1 = bfs(0, 0, n-1, m-1) # 출발지에서 도착지까지
res2 = bfs(0, 0, knife[0], knife[1]) + (n-knife[0]-1) + (m-knife[1]-1) # 출발지에서 칼까지 + 칼에서 도착지까지 최단거리
ans = min(res1, res2)
print(ans if ans <= t else "Fail")