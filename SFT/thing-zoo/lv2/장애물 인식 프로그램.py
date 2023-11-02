from collections import deque
def bfs(i, j):
  dx = [1, 0, -1, 0]
  dy = [0, -1, 0, 1]
  q = deque()
  q.append((i, j))
  visited[i][j] = True
  result = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if not visited[nx][ny] and board[nx][ny]:
            visited[nx][ny] = True
            result += 1
            q.append((nx, ny))
    return result

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            count = bfs(i, j)
            if count > 0: answer.append(count)
answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))