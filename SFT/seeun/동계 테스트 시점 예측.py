import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
  queue = deque()
  visited = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)] # 공기와 몇칸 맞닿아 있는지
  after = [b[:] for b in board] # 얼음이 녹은 이후의 상태
  cnt = 0 # 현재 시점에서 녹은 얼음의 수

  queue.append([x, y])
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 1: # 공기에서 주변을 봤는데 얼음이 있으면 바깥쪽에 있는 얼음임
          cnt += 1
          count[nx][ny] += 1
          if count[nx][ny] == 2:
            after[nx][ny] = 0
        elif board[nx][ny] == 0 and not visited[nx][ny]: # 공기이면 탐색 계속함
          queue.append([nx, ny])
          visited[nx][ny] = True
        
          
  return cnt, after


time = 0
while True:
  cnt, after = bfs(0, 0)
  board = [a[:] for a in after]
  if cnt == 0:
    break
  time += 1
print(time)