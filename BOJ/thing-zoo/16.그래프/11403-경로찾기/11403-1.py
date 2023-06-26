def dfs(i, j): # i -> j 경로 여부 찾기
    visited[i] = True
    stack = [i]
    while stack:
        x = stack.pop()
        for y in range(n):
            if graph[x][y]: # x -> y
                if y == j: return True
                if not visited[y]:
                    visited[y] = True
                    stack.append(y)
    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        visited = [False]*n
        if dfs(i, j): print(1, end=' ') # 경로가 있으면 1
        else: print(0, end=' ') # 경로가 없으면 0
    print()