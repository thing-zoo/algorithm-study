import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [] # 이전 치즈 상태 저장
melt = [] # 녹는 치즈 바로바로 반영
for _ in range(n):
    cheese = list(map(int, input().split()))
    board.append(cheese)
    melt.append(cheese)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False]*m for _ in range(n)]

def bfs(x, y):
    global visited, piece
    piece = 0 
    queue = deque()

    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if board[nx][ny] == 0: # 공기이면
                    if not visited[nx][ny]: # 아직 방문하지 않은 곳이면
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                else: # 공기와 맞닿아있는 치즈이면
                    visited[nx][ny] += 1 # 공기와 닿아잇는 부분이 몇개인지
                    if visited[nx][ny] >= 2: # 두개 이상이면
                        piece += 1 # 녹이기
                        melt[nx][ny] = 0 # 녹음 표시
piece = 1
ans = 0
time = 0
while piece > 0:
    time += 1
    visited = [[0] * m for _ in range(n)]

    bfs(0, 0) # 0, 0부터 시작해서 공기에 닿은 부분만 탐색
    board = [m[:] for m in melt] # 녹은 치즈 상태 복사

    if piece == 0:
        break

print(time-1)
