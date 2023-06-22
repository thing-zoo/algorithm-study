n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 알고리즘 사용
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()