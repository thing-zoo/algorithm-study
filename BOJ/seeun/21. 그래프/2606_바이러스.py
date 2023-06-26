def dfs(node):
    if not visited[node]: # 방문안한 노드이면 
        visited[node] = True # 방문 처리후
        if graph[node]: # 연결된 노드 방문
            for i in graph[node]:
                if not visited[i]:
                    dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

stack = []
visited = [False]*n
dfs(0)
print(visited.count(True)-1)