n, m = map(int, input().split())
graph = [[n+n]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n):
    graph[i][i] = 0

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 각 사람마다 케빈 베이컨의 수 구하기: 사람마다 몇단개 거치는지 모두 더함
mini = []
for i in range(n):
    mini.append(sum(graph[i]))

# 그중 제일 먼저 나오는 최솟값의 인덱스 출력
print(mini.index(min(mini))+1)
# print(graph)