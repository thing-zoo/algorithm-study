from collections import deque
def bfs(x, dir): # 인덱스, 방향에 대해
    q = deque()
    visited = [False]*4
    q.append([x, dir])
    visited[x] = True  # 방문표시
    while q:
        x, dir = q.popleft()
        for dx in (1, -1):
            nx = x + dx
            if 0 <= nx < 4 and not visited[nx]: # 범위내 방문 안한 것이면
                if dx == 1: # 우측
                    if gears[x][2] != gears[nx][6]: # 상극이면
                        visited[nx] = True
                        q.append([nx, -dir])
                elif dx == -1: # 좌측
                    if gears[x][6] != gears[nx][2]: # 상극이면
                        visited[nx] = True
                        q.append([nx, -dir])
        gears[x].rotate(dir) # 회전
gears = []
for _ in range(4):
    gear = deque(list(input()))
    gears.append(gear)
k = int(input())
for _ in range(k):
    i, dir = map(int, input().split())
    bfs(i-1, dir)
answer = 0
for i in range(4):
    if gears[i][0] == "1": # 12시 방향이 S극이면
        answer += 2 ** i
print(answer)