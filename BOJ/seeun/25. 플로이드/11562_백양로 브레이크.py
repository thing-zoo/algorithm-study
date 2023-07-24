import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    if b:
        graph[u][v] = 0
        graph[v][u] = 0
    else:
        graph[u][v] = 0
        graph[v][u] = 1 # 역방향을 뚫어줘야함
    

for i in range(n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    print(graph[a][b])
