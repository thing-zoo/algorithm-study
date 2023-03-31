from collections import deque

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

hx = [-2, -2, -1, 1, 2, 2, -1, 1]
hy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(x, y, s):
    queue.append([x,y, s])
    cnt=[[[0] * (s+1) for _ in range(m)] for _ in range(n)]

    while queue:
        x, y, k= queue.popleft()
        if x == n-1 and y == m-1:
            return cnt[x][y][k]
        if 0<k: # 말처럼 갈 수 있으면
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0<= nx < n and 0<= ny <m and cnt[nx][ny][k-1] == 0 and box[nx][ny] ==0: # 갈 수 있는 길이면 / 레이어마다 말처럼 갈 수 있는 위치 한 번씩 찍기..?
                    queue.append([nx, ny, k-1])
                    cnt[nx][ny][k-1] = cnt[x][y][k] + 1
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny <m and cnt[nx][ny][k] == 0 and box[nx][ny] ==0: # 갈 수 있는 길이면
                queue.append([nx, ny, k])
                cnt[nx][ny][k] = cnt[x][y][k] + 1
    return -1

k = int(input())
m, n = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

print(bfs(0, 0, k))