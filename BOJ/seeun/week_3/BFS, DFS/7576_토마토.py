from collections import deque

queue = deque()
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cntDate = 0

def bfs():
    global cntDate
    while True:
        templen = len(queue)
        for _ in range(templen):
            i, j = queue.popleft()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx<0 or ny<0 or nx >= n or ny >= m:
                    continue
                if box[nx][ny] == 1:
                    continue
                if box[nx][ny] == -1:
                    continue
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    queue.append([nx, ny])
        if len(queue) < 1:
            return True
        cntDate +=1

m, n = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
bfs()
check = 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 1 or box[i][j] == -1:
            continue
        else:
            check = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and check != -1:
           print(-1)
           check = -1
           break

if check == 1:
    print(cntDate)
elif check == 0:
    print(0)