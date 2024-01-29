from collections import deque
def bfs():
    q = deque()
    q.append([1,1])
    light[1][1] = 1
    result = 1
    while q:
        y, x = q.popleft()
        for a, b in switch[y][x]: # 스위치가 있고
            if not light[a][b]: # 불이 안켜져 있으면
                light[a][b] = 1 # 불켜기
                result += 1     # 불 개수 카운트
                for i in range(4): # 상하좌우 확인
                    na, nb = a + dy[i], b + dx[i]
                    if 1 <= na <= n and 1 <= nb <= n:
                        if visited[na][nb] and light[na][nb]: #방문했고 불이 켜져있으면
                            q.append([na, nb]) #재방문해야할수있으므로 큐에 넣기
        for i in range(4): # 상하좌우 확인
            ny, nx = y + dy[i], x + dx[i]
            if 1 <= ny <= n and 1 <= nx <= n:
                if not visited[ny][nx] and light[ny][nx]: #방문 안했고 불이 켜져있으면
                    visited[ny][nx] = 1 # 방문 표시
                    q.append([ny, nx])  # 큐에 넣기
    return result

dx = [1,0,-1,0]; dy = [0,1,0,-1]
n, m = map(int, input().split())
switch = [ [ [] for _ in range(n+1) ] for _ in range(n+1) ]
light = [ [0]*(n+1) for _ in range(n+1) ]
visited = [ [0]*(n+1) for _ in range(n+1) ]
result = 0
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switch[x][y].append([a,b])
print(bfs())