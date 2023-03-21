from collections import deque
def bfs():
    q = deque([n])
    dist[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x]-1)
            break
        for nx in (x+1, x-1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                if nx == x*2:
                    dist[nx] = dist[x]
                    q.appendleft(nx)
                else:    
                    dist[nx] = dist[x] + 1
                    q.append(nx)
MAX = 10 ** 5
dist = [0] * (MAX+1)
n, k = map(int, input().split()) # N:수빈 위치, K:동생 위치
bfs()