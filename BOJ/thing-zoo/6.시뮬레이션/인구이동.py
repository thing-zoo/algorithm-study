from collections import deque
def bfs(a, b):
    q = deque(); q.append([a, b])
    visited[a][b] = True
    union = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    union.append([nx, ny])
    if union:
        union.append([a, b])
        k = 0
        for x, y in union:
            k += graph[x][y]
        k //= len(union)
        for x, y in union:
            graph[x][y] = k
        return True
    else:
        return False

dx = [1,0,-1,0]; dy = [0,1,0,-1]
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
day = 0
while True:
    flag = True
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j): flag = False
                else: visited[i][j] = False
    if flag: break
    else: day += 1
print(day)