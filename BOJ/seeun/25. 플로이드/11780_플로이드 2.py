import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
road = [[[i] for _ in range(n+1)] for i in range(n+1)] # 경로 저장할 배열

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
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                road[i][j] = road[i][k] + road[k][j]

# 가중치 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
            print(0, end =" ")
        else:
            print(graph[i][j], end=" ")
    print()

# 경로 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 0: # i-j가 불가능하면 0출력
            print(0)
            continue
        else: # 아니면 
            road[i][j].append(j) # 도착지 추가하고 출력
            print(len(road[i][j]), *road[i][j])
