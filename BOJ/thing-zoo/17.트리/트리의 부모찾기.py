from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    q = deque([1])
    parents[1] = -1 # 방문표시
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not parents[v]: # 방문 안한 정점이면
                parents[v] = u # 부모 저장
                q.append(v)

n = int(input())
graph = [[] for _ in range(n+1)] # 인접리스트
parents = [0]*(n+1) # 방문&부모배열
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs() # 루트(1)에서부터 부모확인
for i in range(2, n+1):
    print(parents[i])