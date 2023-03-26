from collections import deque

queue = deque()
dz = [-1, 0, 0, 0, 0, 1]
dx = [0, -1, 0, 1, 0, 0]
dy = [0, 0, 1, 0, -1, 0]

time = 0
def bfs(i,j, k):
    global time
    queue.append([i, j, k, time])
    building[i][j][k] = '#' # 출발한 점 벽으로 바꾸기
    while queue:
        i, j, k, time = queue.popleft()
        time += 1
        for t in range(6):
            nz = i + dz[t]
            nx = j + dx[t]
            ny = k + dy[t]

            if nz<0 or nx<0 or ny<0 or nz>=h or nx>=r or ny>=c:
                continue
            if building[nz][nx][ny] == '#':
                continue
            if building[nz][nx][ny] == "E":
                return "Escaped in "+str(time)+" minute(s)."
            if building[nz][nx][ny] == '.':
                building[nz][nx][ny] = '#'
                queue.append([nz, nx, ny, time])
    return "Trapped!"

h, r, c = map(int, input().split())
while h!=0 or r!=0 or c!=0:

    building = []
    for i in range(h):
        tmp = []
        for j in range(r):
            tmp.append(list(input()))
        building.append(tmp)
        input()

    queue = deque()
    time = 0
    for i in range(h):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == "S":
                    print(bfs(i, j, k))

    h, r, c = map(int, input().split())