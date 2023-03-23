from collections import deque
def bfs_bridge(area, answer):
    q = deque()
    dist = [ [-1]*n for _ in range(n) ] # 방문 안한 표시(바다)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == area: # 현재섬만 넣기
                q.append([i,j]) 
                dist[i][j] = 0  # 방문 표시
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] == -1 and graph[ny][nx] == 0: # 방문 안한 바다일 경우
                    dist[ny][nx] = dist[y][x] + 1 # 거리 증가
                    q.append([ny, nx])
                elif graph[ny][nx] > 0 and graph[ny][nx] != area: # 다른 섬인 경우
                    answer = min(answer, dist[y][x]) # 현재값과 비교하여 작을 경우 넣어준다
                    return answer
def bfs(i,j):
    q = deque()
    q.append([i,j])
    graph[i][j] = area + 1
    visited[i][j] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = area + 1 # 숫자로 구분해주기
                    visited[ny][nx] = 1
                    q.append([ny, nx])

dx = [1,0,-1,0]
dy = [0,1,0,-1]
n = int(input())
graph = []
answer = n ** n
visited = [ [0]*n for _ in range(n) ]
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 섬 구분해주기
area = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            bfs(i, j)
            area += 1

# 두 섬 간 최단 거리 구하기
for i in range(1, area):
    answer = bfs_bridge(i, answer)
print(answer)