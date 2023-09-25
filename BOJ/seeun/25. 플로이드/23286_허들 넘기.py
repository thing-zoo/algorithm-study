import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] + graph[k][j] < float('inf'): # 갈수 있는 허들이면
                tmp = max(graph[i][k], graph[k][j]) # k를 거쳐서 가는 것 이면 두 구간 중 가장 높은 허들 높이
                graph[i][j] = min(graph[i][j], tmp) # 기존 루트 vs k거쳐서 가는것 둘중에 더 낮은 허들 높이
                

for _ in range(t):
    a, b = map(int, input().split())
    print(graph[a][b] if graph[a][b] < float('inf') else -1)