from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False]*n
answer = 0

def bfs(i):
    q = deque([i])
    visited[i] = True
    while q:
        x = q.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    

for _ in range(m):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

for i in range(n):
    if not visited[i]:
        bfs(i)
        answer+=1
print(answer)