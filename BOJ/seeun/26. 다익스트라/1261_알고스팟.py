from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1,  0]
dy = [0, 1, 0, -1]
broken = 0
visited = []
def bfs(x, y):
    global broken, visited
    queue = deque()
    visited = [[-1] * m for _ in range(n)] # 최소 몇개를 부숴야 그 자리에 갈 수 있는지 체크
    visited[x][y] = 0 # 시작점은 0

    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == -1: # 아직 방문하지 않은 곳이면
                    if board[nx][ny] == '1': # 벽이면 부수고 가야함
                        visited[nx][ny] = visited[x][y] + 1 # 이전 개수 +1
                        queue.append([nx, ny])
                    else: # 벽이 아니라면
                        visited[nx][ny] = visited[x][y] # 이전개수와 동일하게 저장
                        queue.appendleft([nx, ny]) # 최소로 벽을 부수어야함으로 큐의 제일 앞에 집어넣음

bfs(0, 0)
print(visited[n-1][m-1])