from collections import deque
import sys

res = 0
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    global maze
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append([nx, ny])

    return maze[n-1][m-1]

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

maze = []
for i in range(n):
    tmp = list(map(int, input().rstrip()))
    maze.append(tmp)

print(check(0, 0))
