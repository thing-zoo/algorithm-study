from collections import deque
import sys
n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
  global visited
  queue = deque()
  cnt = 1
  queue.append([x, y])
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny] and board[nx][ny] == 1:
          visited[nx][ny] = True
          queue.append([nx, ny])
          cnt += 1
  return cnt
  
visited = [[False] * n for _ in range(n)]
ans = 0
cntlist = []
for i in range(n):
  for j in range(n):
    if not visited[i][j] and board[i][j] == 1:
      ans += 1
      tmp = bfs(i, j)
      cntlist.append(tmp)

print(ans)
cntlist.sort() # 오름차순 정렬
print("\n".join(map(str, cntlist)))