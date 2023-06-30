from collections import deque
def bfs(i): # 회원 i의 점수 구하기
    dist = [-1]*(n+1)
    dist[i] = 0
    q = deque([i])
    while q:
        x = q.popleft()
        for y in graph[x]:
            if dist[y] == -1: # 방문 안하면
                dist[y] = dist[x] + 1
                q.append(y)
    return max(dist)

n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    i, j = map(int, input().split())
    if i == j == -1: break
    graph[i].append(j)
    graph[j].append(i)

result = [1e9]+[0]*n # 회원별 점수
for i in range(1, n+1):
    result[i] = bfs(i)

min_socre = min(result)
answer = []
for i in range(1, n+1):
    if result[i] == min_socre:
        answer.append(i)
print(min_socre, len(answer))
print(" ".join(map(str, answer)))