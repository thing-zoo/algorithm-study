from collections import deque
def bfs(x, graph): # 정점 x 의 하위 노드 개수 구하기
    visit[x] = True
    q = deque([x])
    count = 0
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not visit[u]:
                visit[u] = True
                count += 1
                q.append(u)
    return count

n, m = map(int, input().split())
smaller_than = [[] for _ in range(n)]
bigger_than = [[] for _ in range(n)]
for _ in range(m):
    v, u = map(int, input().split())
    smaller_than[v-1].append(u-1)
    bigger_than[u-1].append(v-1)

mid = (n + 1)//2
answer = 0
for i in range(n):
    visit = [False]*n
    if bfs(i, bigger_than) >= mid:
        answer += 1
    if bfs(i, smaller_than) >= mid:
        answer += 1
print(answer)