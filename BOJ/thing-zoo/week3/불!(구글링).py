from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque(F)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not dist_f[ny][nx] and graph[ny][nx] != "#":
                    dist_f[ny][nx] = dist_f[y][x] + 1
                    q.append([ny, nx])
    q = deque(J)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not dist_j[ny][nx] and graph[ny][nx] != "#":
                    if not dist_f[ny][nx] or dist_j[y][x] + 1 < dist_f[ny][nx]:
                        dist_j[ny][nx] = dist_j[y][x] + 1
                        q.append([ny, nx])
            else:
                return dist_j[y][x]
    return "IMPOSSIBLE"

dx = [1,0,-1,0]
dy = [0,1,0,-1]
r, c = map(int, input().split())    # r:행, c:열
graph = []                          # #:벽, .:길, J:지훈이, F:불
dist_f = [ [0]*c for _ in range(r) ]
dist_j = [ [0]*c for _ in range(r) ]
J = []; F = []
for i in range(r):
    graph.append(list(input().rstrip()))
    for j in range(c):
        if graph[i][j] == "J":
            J.append([i,j])
            dist_j[i][j] = 1
        elif graph[i][j] == "F":
            F.append([i,j])
            dist_f[i][j] = 1
print(bfs())