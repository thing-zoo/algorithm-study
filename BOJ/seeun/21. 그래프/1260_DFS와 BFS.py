from collections import deque

def bfs(start):
    global n
    queue = deque()
    visited = [False]*n
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft() # 큐 앞에서부터 꺼내오기
        print(node+1, end=" ")
        if graph[node]:
            for v in graph[node]: # 현재 노드에 연결된 모든 노드 큐에 넣기
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

def dfs(start):
    global visited
    if not visited[start]: # 아직 방문하지 않은 노드라면
        visited[start] = True # 방문처리
        print(start+1, end=" ")
        for v in graph[start]: # 현재 노드에 연결된 노드들 확인
            if not visited[v]:
                dfs(v) # 연결된 노드 중 하나로 변경하여 다시 탐색

n, m, s = map(int, input().split())
s -= 1
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    graph[i].sort() # 여러개가 있을 경우 작은 노드부터 방문

visited = [False] * n
dfs(s)
print()
bfs(s)
