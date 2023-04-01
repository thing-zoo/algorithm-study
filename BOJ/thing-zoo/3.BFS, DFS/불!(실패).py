from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = start
    while q:
        y, x, t = q.popleft()
        if t > 0 and graph[y][x] != "F":
            if y == 0 or y == r-1 or x == 0 or x == c-1:
                return t
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != "#":
                if t > 0 and graph[ny][nx] == ".":
                    q.append([ny, nx, t+1])
                elif t == -1 and graph[ny][nx] != "F":
                    q.append([ny, nx, t])
                graph[ny][nx] = graph[y][x]
    return "IMPOSSIBLE"

dx = [1,0,-1,0]
dy = [0,1,0,-1]
r, c = map(int, input().split())    # r:행, c:열
graph = []                          # #:벽, .:길, J:지훈이, F:불
start = deque()                     # 시작지점
for i in range(r):
    graph.append(list(input().rstrip()))
    for j in range(c):
        if graph[i][j] == "J":
            start.appendleft([i, j, 1])
        elif graph[i][j] == "F":
            start.append([i, j, -1])
print(bfs())