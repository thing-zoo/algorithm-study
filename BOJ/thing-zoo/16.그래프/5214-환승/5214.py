from collections import deque
# n: 역의 수 (<= 1e5)
# k: 하이퍼튜브가 서로 연결하는 역의 수 (<=1e3)
# m: 하이퍼튜브의 수 (<=1e3)
n, k, m = map(int, input().split())
adj = [[] for _ in range(n+m+1)] # 하이퍼튜브 또한 역으로 취급

def bfs():
    visited = [False]*(n+m+1)
    visited[1] = True
    q = deque([(1, 1, visited)]) # 정점, 거리, 방문배열
    while q:
        x, d, v = q.popleft()
        if x == n: # 마지막역 도착
            return d # 종료
        for y in adj[x]: # 인접한 역 확인
            if not v[y]:
                v[y] = True
                if y > n: q.append((y, d, v)) # 하이퍼튜브는 거리 계산안함
                else: q.append((y, d+1, v))
    return -1 # 불가능한 경우

# 인접리스트 만들기
for i in range(1, m+1):
    adj[n+i] = list(map(int, input().split()))
    for j in adj[n+i]:
        adj[j].append(n+i)

print(bfs())
