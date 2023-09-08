from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 바이러스를 놓을 수 있는 공간 위치 저장(바이러스위치, 벽 위치)
candi = []
virus = [[float('inf')] * n for _ in range(n)]
empty = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus[i][j] = '*' # 바이러스가 있는 곳은 '*'으로 세팅
            candi.append([i, j])
        elif board[i][j] == 0: # 빈칸 카운트
            empty += 1

if empty == 0: # 빈칸이 하나도 없으면 0임
    print(0)
    exit()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(loc):
    global virus

    queue = deque()
    for x, y in loc:
        virus[x][y] = 0 # 바이러스 놓은 곳은 활성(0) 표시
        queue.append([x, y, 0]) # 위치와 초기 시간 큐에 넣기

    while queue:
        x, y, time = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<= nx < n) or not (0<= ny < n):
                continue
            if board[nx][ny] == 1:
                continue
            if virus[nx][ny] == '*' or  virus[nx][ny] == float('inf'): # 아직 안옮겼거나 비활성 바이러스가 있는 곳이면
                virus[nx][ny] = time + 1 # 활성화 시키고 큐에 넣기
                queue.append([nx, ny, time +1])

ans = float('inf')
maxtmp = 0
for loc in combinations(candi, m):

    # 바이러스 퍼뜨리기
    bfs(loc)

    # 가장 오래걸리는 시간 찾기 & 바이러스 배열 초기화
    tmp = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 : # 빈칸인 곳만 확인
                tmp = max(virus[i][j], tmp) # 가장 늦게 도달한 곳 시간 측정

            # 바이러스 배열 초기화
            if board[i][j] == 2:
                virus[i][j] = '*'
            else:
                virus[i][j] = float('inf')

    ans = min(tmp, ans) # 가장 늦게 도달한 시간 중에 최솟값

print(ans if ans != float('inf') else -1)