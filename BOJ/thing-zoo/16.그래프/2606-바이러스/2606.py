def dfs(v):
    stack = [v]
    visited[v] = True
    answer = 0
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if not visited[y]:
                stack.append(y)
                visited[y] = True
                answer += 1
    return answer

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

print(dfs(1))