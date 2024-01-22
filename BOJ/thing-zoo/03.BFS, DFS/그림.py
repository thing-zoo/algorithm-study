from collections import deque
def bfs(y, x):
    answer = 1
    q = deque([[y,x]])
    graph[y][x] = 0
    while q:
        y,x = q.popleft()
        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx]:
                    graph[ny][nx] = 0
                    q.append([ny, nx])
                    answer += 1
    return answer

dir = [[0,1],[-1,0],[0,-1],[1,0]]
n, m = map(int, input().split()) # n: 세로 m: 가로
graph = [ ]
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = []
for y in range(n):
    for x in range(m):
        if graph[y][x]:
            result.append(bfs(y, x))
size = len(result) 
print(size)
if size:
    print(max(result))
else:
    print(0)