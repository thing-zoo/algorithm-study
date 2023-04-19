from collections import deque
from itertools import combinations
def bfs(): # 바이러스 영역 세기
    q = deque(virus)
    virus_count = len(virus)
    visited = [[False]*m for _ in range(n)]
    for x, y in virus:
        visited[x][y] = True
    while q:
        x, y = q.popleft()
        if virus_count >= min_virus: # 최소값보다 커질경우
            break # 종료
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == EMPTY:
                    virus_count += 1
                    visited[nx][ny] = True
                    q.append([nx,ny])
    return virus_count

dx = [1,0,-1,0]; dy = [0,1,0,-1]
EMPTY, WALL, VIRUS = 0, 1, 2
n, m = map(int, input().split())
board = []
virus = []
empty = []
wall_count = 0
min_virus = n*m
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == EMPTY:
            empty.append([i,j])
        elif board[i][j] == VIRUS:
            virus.append([i,j])
        else:
            wall_count += 1

for selected in combinations(empty, 3): # 벽 3개 고르기
    for x, y in selected: # 벽 세우기
        board[x][y] = WALL
    min_virus = min(bfs(), min_virus) # 최소 바이러스 영역 구하기
    for x, y in selected: # 되돌리기
        board[x][y] = EMPTY
print(n*m - (wall_count+3) - min_virus)