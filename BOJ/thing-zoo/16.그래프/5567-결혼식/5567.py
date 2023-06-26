def dfs(i):
    visited[i] = True
    stack = [(i, 0)] # i번, 거리
    answer = 0
    while stack:
        x, d = stack.pop()
        if d >= 2: continue # 자신의 친구, 친구의 친구만 가능
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                stack.append((y, d+1))
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