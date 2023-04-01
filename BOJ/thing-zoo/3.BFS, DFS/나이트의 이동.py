from collections import deque
def bfs():
    q = deque([[i, j]])
    dist[j][i] = 1
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            print(dist[b][a]-1)
            break
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < l and 0 <= ny < l:
                if not dist[ny][nx]:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append([nx, ny])

dir = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
t = int(input())
for _ in range(t):
    l = int(input()) # 체스판 한 변의 길이
    i, j = map(int, input().split()) # 현재 위치
    a, b = map(int, input().split()) # 목표 위치
    dist = [ [0] * l for _ in range(l)] 
    bfs()