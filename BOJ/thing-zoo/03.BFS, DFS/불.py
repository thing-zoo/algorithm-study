import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    q = deque(f)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if not dist_f[ny][nx] and graph[ny][nx] != "#":
                    dist_f[ny][nx] = dist_f[y][x] + 1
                    q.append([ny, nx])
    q = deque(s)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if not dist[ny][nx] and graph[ny][nx] != "#":
                    if not dist_f[ny][nx] or dist[y][x] + 1 < dist_f[ny][nx]:
                        dist[ny][nx] = dist[y][x] + 1
                        q.append([ny, nx])
            else:
                return dist[y][x]
    return "IMPOSSIBLE"

dx = [1,0,-1,0]
dy = [0,1,0,-1]
for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = []
    dist = [ [0]*w for _ in range(h) ]
    dist_f = [ [0]*w for _ in range(h) ]
    s = []; f = []
    # .:빈공간, #:벽, @:상근이, *:불
    for i in range(h):
        graph.append(list(input().rstrip()))
        for j in range(w):
            if graph[i][j] == "*":
                f.append([i,j])
                dist_f[i][j] = 1
            elif graph[i][j] == "@":
                s.append([i,j])
                dist[i][j] = 1
    print(bfs())