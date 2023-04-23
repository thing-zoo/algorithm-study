from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global safe_area, visited, virus_cnt
    queue = deque()
    visited[x][y] = True
    queue.append([x, y])
    # virus_cnt += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if lab[nx][ny] == 0 and not visited[nx][ny]: # 연구소 범위 내 & 아무것도 없는 곳이면 퍼져나감
                    visited[nx][ny] = True # 퍼뜨리고
                    queue.append([nx, ny]) # 큐에 넣기
                    virus_cnt += 1 # 안전지역 하나 없앰


# Main
n, m = map(int, input().split())
lab = []
virus = []
wall = []
nothing = []

for _ in range(n):
    lab.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 1:
            wall.append([i, j])
        elif lab[i][j] == 2:
            virus.append([i, j])
        else:
            nothing.append([i, j])

safe_area = -100000
for walls in combinations(nothing, 3):
    # 벽 세우기
    for x, y in walls:
        lab[x][y] = 1

    visited = [[False]*m for _ in range(n)]
    virus_cnt = 0
    # 바이러스 퍼뜨리기
    for i in range(len(virus)):
        if visited[virus[i][0]][virus[i][1]]== False:
            bfs(virus[i][0], virus[i][1])

    # 현재 안전구역의 개수구하고 최댓값과 비교
    tmp_safe = len(nothing) - 3 - virus_cnt # 0이었던 칸 개수 -벽 3개 -바이러스 퍼진 개수  
    safe_area = max(safe_area, tmp_safe)

    # 벽 없애기
    for x, y in walls:
        lab[x][y] = 0

print(safe_area)