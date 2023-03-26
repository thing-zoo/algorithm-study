from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    answer = False
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    cnt = 1
    x = 0
    y = 0
    queue.append([x, y])
    maps[x][y] = 2
    
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            answer = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])
                    
    if answer:
        return maps[n-1][m-1]-1
    else:
        return -1