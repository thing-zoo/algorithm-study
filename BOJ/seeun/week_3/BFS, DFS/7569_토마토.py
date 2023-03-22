from collections import deque

queue = deque()
dz = [-1, 0, 0, 0, 0, 1]
dx = [0, -1, 0, 1, 0, 0]
dy = [0, 0, 1, 0, -1, 0]
cntDate = 0

def bfs():
    global cntDate
    while True:
        templen = len(queue)
        for _ in range(templen):
            i, j, k = queue.popleft()
            for d in range(6):
                nz = i + dz[d]
                nx = j + dx[d]
                ny = k + dy[d]
                if nx<0 or ny<0 or nz <0 or nz >= h or nx >= n or ny >= m:
                    continue
                if box[nz][nx][ny] == 1:
                    continue
                if box[nz][nx][ny] == -1:
                    continue
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    queue.append([nz, nx, ny])
        if len(queue) < 1:
            return True
        cntDate +=1

m, n, h = map(int, input().split())

box = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)
    

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append([i, j, k])
bfs()
check = 1

# 시간 지났는데도 덜 익은 토마토가 있는지 체크
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0 and check != -1:
                print(-1)
                check = -1
                exit()

if check == 1:
    print(cntDate)