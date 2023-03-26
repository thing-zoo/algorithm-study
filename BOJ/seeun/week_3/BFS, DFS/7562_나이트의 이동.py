from collections import deque

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

cnt = 0
def bfs (x, y):
    queue = deque()
    queue.append([x, y])
    global cnt
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        if x == ea and y == eb:
            return chess[x][y]
        for i in range(8):
            if x == ea and y == eb:
                return chess[x][y]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= m:
                continue
            # print(nx, ny)
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y]+1
                queue.append([nx, ny])
            
            # for k in range(m):
            #     print(chess[k])


n = int(input())

for i in range(n):
    m = int(input())
    sa, sb = map(int, input().split())
    ea, eb = map(int, input().split())
    chess = [[0] * m for _ in range(m)]
    chess[sa][sb] = 0
    chess[ea][eb] = 0

    print(bfs(sa, sb))

