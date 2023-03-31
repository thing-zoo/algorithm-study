from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])

    while queue:
        x, y, z = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]+1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny < m and z>0:
                if visited[nx][ny][z-1] == 0 and box[nx][ny] == 1:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    queue.append([nx, ny, z-1])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <n and 0<= ny < m :
                if visited[nx][ny][z] == 0 and box[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
        
    return -1

n, m = map(int, input().split())

box = []
for _ in range(n):
    tmp = list(input())
    box.append(list(map(int, tmp)))

k = 1
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, k))