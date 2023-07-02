from collections import deque
import sys
input = sys.stdin.readline
def bfs(x):
    dist[x] = 0
    q = deque([x])
    max_dist = 0
    while q:
        v = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                max_dist = max(dist[u], max_dist)
                q.append(u)
    return max_dist

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

dist = [-1]*n
max_dist = bfs(0)
node = -1
count = 0
for i in range(n):
    if max_dist == dist[i]:
        if node == -1: node = i+1
        count += 1
print(node, max_dist, count)
