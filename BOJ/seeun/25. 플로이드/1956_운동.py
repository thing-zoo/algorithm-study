import sys
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[float('inf')]*(v+1) for _ in range(v+1)]
parent = [i for i in range(v+1)]
        
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a][b] = c

# 플로이드 진행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = float('inf')
for i in range(1, v+1): # i에서 출발해서 i로 돌아옴 
    ans = min(ans, graph[i][i])

print(ans if ans != float('inf') else -1)