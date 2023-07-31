import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[-1] * (n+1) for _ in range(n+1)] # 원본 그래프를 저장
floyd = [[float('inf')] * (n+1) for _ in range(n+1)] # 플로이드를 진행할 그래프 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = max(graph[a][b], c)
    graph[b][a] = max(graph[b][a], c)
    floyd[a][b] = min(floyd[a][b], c)
    floyd[b][a] = min(floyd[b][a], c)

for i in range(1, n+1):
    floyd[i][i] = 0

# 플로이드 진행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

# 그래프 태우기
ans = float('inf')
for start in range(1, n+1): # 태우는 시작점이 i일 때
    time = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            edge = graph[i][j]
            if floyd[i][j] == float('inf'): # i->j를 잇는 간선이 없으면 패스
                continue
            # 남은 i-j 간선길이: 기존 i-j 간선 길이 - i-j의 최단거리
            remain = edge - (floyd[start][j]-floyd[start][i])
            if remain > 0: # 남은 부분이 있다면
                time = max(time, remain/2 + floyd[start][j]) # 양쪽에서 탈 것이기 때문에 2로 나눠줌
    ans = min(ans, time)

print('%.1f' %ans)