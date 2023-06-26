from collections import deque
import sys
input = sys.stdin.readline
n, m ,v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

def dfs(v):
    stack = [v]
    while stack:
        x = stack.pop()
        if visited[x]: continue
        visited[x] = True
        print(x, end=' ')
        for y in range(n, 0, -1):
            if not visited[y] and graph[x][y]:
                stack.append(y)

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in range(1, n+1):
            if not visited[y] and graph[x][y]:
                visited[y] = True
                q.append(y)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

visited = [False]*(n+1)
dfs(v)
print()

visited = [False]*(n+1)
bfs(v)
