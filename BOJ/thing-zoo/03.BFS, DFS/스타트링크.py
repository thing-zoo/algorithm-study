from collections import deque
def bfs():
    q = deque([s])
    dist[s] = 1
    while q:
        x = q.popleft()
        if x == g:
            print(dist[x]-1) # 맨 처음 위치는 빼주기
            return
        for nx in (x+u, x-d):
            if 1 <= nx <= f:
                if not dist[nx]:
                    dist[nx] = dist[x] + 1
                    q.append(nx)
    print("use the stairs")

# f:전체층, s:현재층, g:목표층, u:올라가는 층수, d: 내려가는 층수
MAX = 10 ** 6
f,s,g,u,d = map(int, input().split())
dist = [0] * (MAX+1) # 이동횟수 및 방문 표시
bfs()