from collections import deque
n = int(input())
graph = [[n+n]*n for _ in range(n)] # 최댓값으로 초기화

a, b = map(int, input().split())
while a!=-1 or b!=-1:
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1
    a, b = map(int, input().split())

for i in range(n): # 자기자신<->은 0으로 처리
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

score = [0]*n # 각 노드마다 최대 점수를 저장함
for i in range(n):
    score[i] = max(graph[i])
print(min(score), score.count(min(score))) # 최솟값과 개수 출력
for i in range(n):
    if score[i] == min(score): # 최솟값인 사람들 모두 출력
        print(i+1, end=" ")