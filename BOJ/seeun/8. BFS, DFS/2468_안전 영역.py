from collections import deque
from copy import deepcopy

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
town = []
res = []

def bfs(i, j, h):
    global visited, cnt
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if nx<0 or ny<0 or nx>=n or ny >= n:
                continue
            if town[nx][ny] > h and visited[nx][ny]==0: # 안전한높이이고 아직 방문하지 않았으면.
                queue.append([nx, ny])
                visited[nx][ny] = 1
            elif town[nx][ny] <= h:
                town[nx][ny] = 0

n = int(input())
maxh = -1
town = []
for i in range(n):
    town.append(list(map(int, input().split())))
    if maxh<max(town[i]):
        maxh = max(town[i])


visited = [[0]*n for _ in range(n)]
for c in range(0, maxh+1): # 0 부터 해야 비가 안올 때 아무것도 안 잠기는 케이스도 카운트 가능
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if c< town[i][j] <=maxh and visited[i][j] == 0: #밭으로 따지면 1일때: 갈수있는 길
                bfs(i, j, c)
                cnt +=1 # 구역 몇갠지 cnt

    res.append(cnt)

print(max(res))