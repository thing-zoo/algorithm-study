import math
n, m = map(int, input().split())
graph_big = [[float('inf')]*n for _ in range(n)]
graph_small = [[float('inf')]*n for _ in range(n)]

# 그래프 생성
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph_big[a][b] = 1
    graph_small[b][a] = 1

# 자기자신 처리
for i in range(n):
    graph_big[i][i] = 0
    graph_small[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph_big[i][j] = min(graph_big[i][j], graph_big[i][k]+graph_big[k][j])
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph_small[i][j] = min(graph_small[i][j], graph_small[i][k]+graph_small[k][j])

answer = 0
for i in range(n):
    tmp = graph_big[i].count(float('inf'))
    # print(i,"보다 작은것 개수", n-tmp-1)
    if n-tmp-1 >= math.ceil(n/2):
        answer += 1
    tmp = graph_small[i].count(float('inf'))
    # print(i,"보다 큰것 개수", n-tmp-1)
    if n-tmp-1 >= math.ceil(n/2):
        answer += 1

print(answer)