from collections import deque
def solution(maps):
    n = len(maps); m = len(maps[0])
    dist = [ [0]*m for _ in range(n) ]
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    q = deque([[0,0]])
    dist[0][0] = 1
    while q:
        y, x = q.popleft()
        if y == n-1 and x == m-1:
            return dist[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not dist[ny][nx] and maps[ny][nx]:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append([ny,nx])
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))