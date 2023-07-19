import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

# 그래프 초기값 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# i->i 0으로 처리
for i in range( n+1):
    graph[i][i] = 0

# 플로이드 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            print(0, end =" ")
        else:
            print(graph[i][j], end=" ")
    print()