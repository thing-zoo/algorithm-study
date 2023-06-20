from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*n
cnt = 0
for i in range(n): # 0번부터 하나씩 연결된 노드 확인
    if not visited[i]: # 현재 노드가 아직 체크 안한 노드이면
        q = deque()
        cnt += 1 # 연결요소 개수 +1
        visited[i] = True # 방문표시
        q.append(i) # 큐에 넣기
        while q:
            node = q.popleft() # 현재 연결요소에 연결된 노드 하나 꺼내옴
            for n in graph[node]: # 그 노드와 연결된 노드들 체크
                if not visited[n]: # 방문 안한 노드이면 
                    q.append(n) # 큐에 넣고
                    visited[n] = True # 방문체크

print(cnt)