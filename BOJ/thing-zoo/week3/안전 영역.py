from collections import deque
def bfs(i, j):
    q = deque([[i, j]])
    dist[i][j] = 1
    while q:
        y, x = q.popleft()
        for d in dir:
            ny = y + d[1]
            nx = x + d[0]
            if 0 <= ny < n and 0 <= nx < n:
                if not dist[ny][nx] and graph[ny][nx] > k:
                    dist[ny][nx] = 1
                    q.append([ny, nx])

dir = [[1,0],[0,1],[-1,0],[0,-1]]
n = int(input())
graph = []
max_height = 0 # 주어진 배열의 최대높이
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    a = max(data)
    if a > max_height: max_height = a

answer = 0 # 최대 안전영역 수
for k in range(max_height): # 최대높이-1까지
    dist = [ [0]*n for _ in range(n) ]
    count = 0
    for i in range(n):
        for j in range(n):
            if not dist[i][j] and graph[i][j] > k:
                bfs(i, j)
                count += 1
    if count > answer: answer = count
print(answer)