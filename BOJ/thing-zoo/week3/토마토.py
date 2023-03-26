from collections import deque
def bfs():
    q = deque(start)
    answer = 0
    while q:
        y, x = q.popleft()
        for d in dir:
            ny = y + d[1]
            nx = x + d[0]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    if answer < graph[ny][nx]: answer = graph[ny][nx]
                    q.append([ny, nx])
    if answer == 0:
        return 0
    else:
        return answer - 1

dir = [[1,0],[0,1],[-1,0],[0,-1]]
m, n = map(int, input().split())    # m:가로, n:세로
graph = [ [0]*m for _ in range(n) ] # 상자
start = []                          # 익은 토마토들
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            start.append([i,j])
        graph[i][j] = tmp[j]

answer = bfs()

flag = 0
for i in range(n):
    if 0 in graph[i]:
        flag = 1
if flag:
    print(-1)
else:
    print(answer)