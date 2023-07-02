from collections import deque
import sys
input = sys.stdin.readline
def bfs(x):
    visit = [False]*(n+1)
    visit[x] = True
    q = deque([x])
    count = 1
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not visit[u]:
                visit[u] = True
                q.append(u)
                count += 1
    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[j].append(i)

max_count = 1
answer = []
for i in range(1, n+1):
    count = bfs(i)
    if max_count < count:
        max_count = count
        answer = [i]
    elif max_count <= count:
        answer.append(i)
print(" ".join(map(str, answer)))