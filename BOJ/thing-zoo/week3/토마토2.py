from collections import deque
def bfs():
    q = deque(start)
    answer = 0
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    if answer < graph[nz][ny][nx]: answer = graph[nz][ny][nx]
                    q.append([nz, ny, nx])
    if answer == 0:
        return 0
    else:
        return answer - 1

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
m, n, h = map(int, input().split()) # m:가로, n:세로, h:높이
graph = [ [0]*n for _ in range(h) ] # 상자
start = []                          # 익은 토마토들
for i in range(h):
    for j in range(n):
        tmp = list(map(int, input().split()))
        for k in range(m):
            if tmp[k] == 1:
                start.append([i,j,k])
        graph[i][j] = tmp

answer = bfs()

flag = 0
for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            flag = 1
if flag:
    print(-1)
else:
    print(answer)