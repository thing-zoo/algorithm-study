import sys
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드로 거리 최솟값 구해놓기
for p in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])

ans = float('inf')
visited = [False] * n
# 백트래킹으로 시간 최소값 구하기
def visit(start, time):
    global ans
    if visited.count(False) == 0: # 모든 지점을 방문했으면
        ans = min(ans, time)
        return
    for i in range(n):
        if i == start or visited[i]: # 출발지점과 도착지점이 같음 || 이미 방문한 지점이면 패스
            continue
        visited[i] = True # 현재지점 방문
        visit(i, time + graph[start][i]) # 백트래킹
        visited[i] = False # 현재지점 방문 취소

visited[k] = True # 시작지점 방문처리
visit(k, 0)
print(ans)
