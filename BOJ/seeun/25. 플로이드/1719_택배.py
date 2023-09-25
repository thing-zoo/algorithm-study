import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

route = [[i for i in range(n+1)] for _ in range(n+1)] # 최소 경로로 가기 위해 이 다음에 가야할 곳
for i in range(1, n+1):
    route[i][i] = 0
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]: # k를 거쳐서 가는 것이 더 작으면
                route[i][j] = route[i][k] # k를 가기 위해 가장 먼저 들러야하는 곳을 저장함
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    route[i][i] = '-'
    print(" ".join(map(str, route[i][1:])))