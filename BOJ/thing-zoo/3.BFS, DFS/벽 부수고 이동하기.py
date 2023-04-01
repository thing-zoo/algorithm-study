from collections import deque
def bfs():
    q = deque()
    q.append([1,1,0])
    dist[1][1][0] = 1 #방문 겸 거리 표시
    while q:
        y, x, w = q.popleft()
        if y == n and x == m:
            return dist[y][x][w]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 1 <= ny <= n and 1 <= nx <= m:
                if not dist[ny][nx][w] and graph[ny][nx] == 0:
                    dist[ny][nx][w] = dist[y][x][w] + 1
                    q.append([ny, nx, w])
                elif w == 0 and graph[ny][nx] == 1:
                    dist[ny][nx][1] = dist[y][x][0] + 1
                    q.append([ny, nx, 1])
    return -1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
n, m = map(int, input().split())
graph = [ [0]*(m+1) for _ in range(n+1)]
dist = [ [ [0] * 2  for _ in range(m+1) ] for _ in range(n+1) ]
for i in range(1,n+1):
    tmp = input()
    for j in range(1,m+1):
        graph[i][j] = int(tmp[j-1])
print(bfs())