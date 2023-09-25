from collections import deque
n, m = map(int, input().split())
turnOn = [[False]*n for _ in range(n)] # 불 켜짐 여부 저장
switch = {} # 방마다 설치된 스위치 정보 저장
for _ in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if (a, b) in switch.keys():
        switch[(a, b)].append([c, d])
    else:
        switch[(a, b)] = []
        switch[(a, b)].append([c, d])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    
    cnt = 1
    queue.append([x, y])
    turnOn[0][0] = True
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()

        # 불 켜기
        if (x, y) in switch.keys(): # 현재 위치에 스위치가 있으면
            for s in switch[(x, y)]:
                if not turnOn[s[0]][s[1]]:
                    turnOn[s[0]][s[1]] = True # 방에 불 켜기
                    cnt += 1
                    for i in range(4): # 불 켠 주변 방 살피기
                        nx = s[0] + dx[i]
                        ny = s[1] + dy[i]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            if visited[nx][ny]: # 이미 방문 했던 곳 다시 살피기
                                queue.append([nx, ny])

        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny] and turnOn[nx][ny]: # 아직 방문 안한곳, 불켜진 곳만 이동
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                
    return cnt

print(bfs(0, 0))
