from collections import deque
def bfs():
    q = deque([n]) # 위치, 걸린시간
    while q:
        x = q.popleft()
        if x == k: # k에 도달하면 탈출
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2): # 이동
            if 0 <= nx <= MAX:
                if not dist[nx]:
                    dist[nx] = dist[x] + 1
                    q.append(nx)
MAX = 10 ** 5
n, k = map(int, input().split())
dist = [0] * (MAX + 1) # 걸린시간 겸 방문표시
bfs()