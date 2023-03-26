import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        sea = 0
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or y>=m:
                continue
            if level[nx][ny] == 0: # 인접한 바다 표면 수 카운트
                sea += 1
            elif level[nx][ny] !=0 and visited[nx][ny] == 0: # 빙산이면 방문체크, ice로 체크하면 이미 녹아있는 상태가 저장되어 있기 때문에 오류남, 꼭 level(작년상태)로 체크
                queue.append([nx, ny])
                visited[nx][ny] = 1
        if ice[x][y] - sea>=0: # 인접한 면 만큼 빙산 녹이기
            ice[x][y] -= sea
        else: # 마이너스가 되면 0으로 처리
            ice[x][y] = 0

n, m = map(int, input().split())
ice = []
level = []
visited = [[0] * m for _ in range(n)]
maxice = -1
for i in range(n):
    ice.append(list(map(int, input().split())))
    if maxice<max(ice[i]):
        maxice = max(ice[i])

level = [tmp[:] for tmp in ice] # 녹이기와 동시에 빙산을 돌면 오류가 생기기 때문에 이전 상태를 저장하는 용도
res=0
y = 0 # year
while True:
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if level[i][j] != 0 and visited[i][j] ==0:
                cnt += 1
                bfs(i, j) # 빙산 발견하면 녹이러 들어감
    if cnt>=2:
        res = y
        print(res)
        break
    elif cnt == 0:
        print(res)
        break
    level = [tmp[:] for tmp in ice] # 1년 지나고 나면 녹은 상태의 빙산을 level에 저장
    y += 1 # year ++
