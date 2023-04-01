from collections import deque
def bfs():
    q = deque([start])
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if graph[nz][ny][nx] == 'E':
                    print("Escaped in %d minute(s)." %(graph[z][y][x] + 1))
                    return
                if graph[nz][ny][nx] == '.':
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append([nz, ny, nx])
    print("Trapped!")

dx = [1, 0, -1, 0, 0, 0] # 동,서,남,북,상,하
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while True:
    L, R, C = map(int, input().split()) # L:층, R:행, C:열
    if L == R == C == 0:
        break
    graph = [[0] * R for _ in range(L)] # #:장애물, .:비어있는칸, S:시작, E:출구
    start = []                          # 시작지점
    for i in range(L):
        for j in range(R):
            tmp = list(input())
            for k in range(C):
                if tmp[k] == 'S':
                    start = [i,j,k] # 시작지점 저장
                    tmp[k] = 0      # 시간 초기화(방문표시)
            graph[i][j] = tmp
        input()
    bfs()