from collections import deque
def bfs():
    q = deque([[n, 0]]) # 위치, 걸린시간
    visited[n] = True 
    while q:
        x = q.popleft()
        if x[0] == k: # k에 도달하면 탈출
            return x[1]
        for i in dir: # 이동
            if i == 2:
                nx = x[0] * 2
            else:
                nx = x[0] + i
            if 0 <= nx <= MAX:
                if not visited[nx]:
                    visited[nx] = True
                    q.append([nx, x[1] + 1])
dir = [ -1, 1, 2 ]
MAX = 10 ** 5
n, k = map(int, input().split())
visited = [False] * (MAX + 1)
print(bfs())