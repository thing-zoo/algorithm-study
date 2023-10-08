# 이분그래프에서 각 정점과 연결된 정점은 다른 집합에 속해야한다.
# 따라서 사이클이 있다면 이분그래프가 아니다.
from collections import deque
import sys
input = sys.stdin.readline
def bfs(x): # 이분그래프 판별
    visited[x] = 1
    q = deque([x])
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not visited[u]: # 방문 안한 정점이면
                # 다른 집합에 넣기
                if visited[v] == 1: visited[u] = 2
                else: visited[u] = 1
                q.append(u)
            elif visited[u] == visited[v]: # 같은 집합(사이클 발생)
                return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        i, j = map(int, input().split())
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)

    visited = [0]*v # 미방문(0), 집합1(1), 집합2(2)
    flag = True
    for i in range(v):
        if not visited[i] and not bfs(i):
            flag = False
            break
    if flag: print("YES")
    else: print("NO")