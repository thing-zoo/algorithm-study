from collections import deque
def bfs(x, y, d):
    visited = [[False]*w for _ in range(h)]
    visited[x][y] = True
    q = deque([(x, y, d, visited, '', 1)]) # 행,열,방향,방문배열,명령어,걸음수
    while q:
        x, y, d, visited, command, count = q.popleft()
        if count == walk: # 로봇 걸음수만큼 도달하면
            return command # 종료
        
        for i in range(4): # 4방향에 대해
            if i == 0: c = 'A'
            elif i == 1: c = 'RA'
            elif i == 2: c = 'RRA'
            else: c = 'LA'
            
            nd = (d+i)%4
            flag = True
            for j in range(1, 3): # 2칸 모두 확인해줘야함
                nx = x + dx[nd]*j
                ny = y + dy[nd]*j
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    flag = False
                    break
                if visited[nx][ny] or board[nx][ny] != '#':
                    flag = False
                    break
            if flag:
                visited[nx-dx[nd]][ny-dy[nd]] = True
                visited[nx][ny] = True
                q.append((nx, ny, nd, visited, command+c, count+2))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
dir = ['^', '>', 'v', '<']
h, w = map(int, input().split())
board = []
walk = 0
for i in range(h):
    board.append(input())
    for j in range(w):
        if board[i][j] == '#':
            walk += 1
            
answer = [0, 0, 0, 'A'*25*25] # 초기위치, 방향, 명령어
for i in range(h):
    for j in range(w):
        if board[i][j] == '#':
            for d in range(4):
                result = bfs(i, j, d)
                if result and len(answer[3]) > len(result):
                    answer = [i, j, dir[d], result]
print(answer[0]+1, answer[1]+1)
print(answer[2])
print(answer[3])