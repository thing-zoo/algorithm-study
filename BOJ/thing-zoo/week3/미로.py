from collections import deque
def bfs(y, x):
    q = deque([[y,x]])
    while q:
        y,x = q.popleft()
        if y == n and x == m:
            break
        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if ny == 1 and nx == 1:
                continue
            if 1 <= ny <= n and 1 <= nx <= m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])
                    
dir = [[0,1],[-1,0],[0,-1],[1,0]]
n,m = map(int, input().split())
graph = [ [0]*(m+1) for _ in range(n+1) ]
for i in range(1, n+1):
    tmp = input()
    for j in range(1, m+1):
        graph[i][j] = int(tmp[j-1])
bfs(1, 1)
print(graph[n][m])