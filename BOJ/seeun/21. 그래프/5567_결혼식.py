n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

def dfs(g, visited, n, depth):
    # print(n, depth)
    if depth == 2:
        return
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
        dfs(g, visited, i, depth+1)

visited = [False]*n
visited[0] = True
dfs(graph, visited, 0, 0)
# print(visited)
print(visited.count(True)-1)