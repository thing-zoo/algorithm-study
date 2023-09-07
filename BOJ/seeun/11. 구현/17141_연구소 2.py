from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 바이러스를 놓을 수 있는 공간 위치 저장
candi = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            candi.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(loc):
    global virus

    queue = deque()
    for x, y in loc:
        virus[x][y] = 0 # 바이러스 놓은 곳은 0으로 표시
        queue.append([x, y, 0]) # 위치와 초기 시간 저장

    while queue:
        x, y, time = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<= nx < n) or not (0<= ny < n):
                continue
            if virus[nx][ny] == float('inf') and board[nx][ny] != 1: # 아직 바이러스를 안옮겼고 빈 칸이면
                virus[nx][ny] = time + 1
                queue.append([nx, ny, time + 1])

ans = float('inf')
maxtmp = 0
for loc in combinations(candi, m):
    virus = [[float('inf')] * n for _ in range(n)]
    bfs(loc)
    tmp = 0
    # 가장 오래걸리는 시간 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] != 1: # 벽이 아닌 곳만 확인
                tmp = max(virus[i][j], tmp)
    ans = min(tmp, ans)

print(ans if ans != float('inf') else -1)