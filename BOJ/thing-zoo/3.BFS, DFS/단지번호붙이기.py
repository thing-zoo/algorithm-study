from collections import deque
def bfs(a, b):
    q = deque([[a, b]])
    graph[a][b] = 0
    answer = 1
    while q:
        y, x = q.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx]:
                    graph[ny][nx] = 0
                    q.append([ny,nx])
                    answer += 1
    return answer

dir = [[1,0],[0,1],[-1,0],[0,-1]]
n = int(input()) # 지도의 크기
graph = [[0]*n for _ in range(n)]
for i in range(n):
    tmp = input()
    for j in range(n):
        graph[i][j] = int(tmp[j])

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            result.append(bfs(i, j))
size = len(result)
print(size)
result.sort()
for i in range(size):
    print(result[i])