from collections import deque
def bfs(y, x):
    q = deque([[y, x]])
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0 <= nx < m: 
                if graph[ny][nx]:
                    graph[ny][nx] = 0
                    q.append([ny, nx])
                    
dir = [[0,1],[-1,0],[0,-1],[1,0]]
t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [ [0] * m for _ in range(n) ]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    answer = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x]:
                bfs(y, x)
                answer += 1
    print(answer)
    
    