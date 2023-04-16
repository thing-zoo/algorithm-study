from collections import deque
n, m = map(int, input().split())

board = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    board.append(list(input()))

# 공 위치 저장
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            redX = i
            redY = j
        if board[i][j] == "B":
            blueX = i
            blueY = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global redY, redX, blueX, blueY, cnt
    queue = deque()
    visited = []
    cnt = 0
    queue.append([redX, redY, blueX, blueY, cnt])
    visited.append([redX, redY, blueX, blueY, cnt])
    while queue:
        redX, redY, blueX, blueY, cnt = queue.popleft()
        
        if cnt >= 10:
            return -1
        cnt += 1
        for i in range(4):
            rnx = redX
            rny = redY
            while True: # 빨간색: 벽 만나거나 구멍 만날때 까지 이동
                rnx += dx[i]
                rny += dy[i]
                if board[rnx][rny] == "#": # 앞쪽이 벽이면 멈춤, 지금자리 큐에 넣기
                    rnx -= dx[i]
                    rny -= dy[i]
                    break
                if board[rnx][rny] == "O": # 구멍이면 빠짐
                    break
            bnx = blueX
            bny = blueY
            while True: # 파란색: 벽 만나거나 구멍 만날때 까지 이동
                bnx += dx[i]
                bny += dy[i]
                if board[bnx][bny] == "#": # 앞쪽이 벽이면 멈춤, 지금자리 큐에 넣기
                    bnx -= dx[i]
                    bny -= dy[i]
                    break
                if board[bnx][bny] == "O": # 구멍이면 빠
                    break
            

        # 여기서 부터 중요
            if board[bnx][bny] == "O": # 파란색이 들어가면 무시
                continue
            if bnx == rnx  and bny == rny: # 같은 위치에 있으면 뒤로 한칸 감
                if abs(redX-rnx)+ abs(redY-rny) < abs(blueX-bnx) + abs(blueY-bny):
                   bnx -= dx[i]
                   bny -= dy[i]
                else:
                    rnx -= dx[i]
                    rny -= dy[i]
            if board[rnx][rny] == "O": # 그랬는데 만약에 빨간색이 홀에 들어가면 끝
                return cnt  
            if [rnx, rny, bnx, bny, cnt] not in visited:
                queue.append([rnx, rny, bnx, bny, cnt])
                visited.append([rnx, rny, bnx, bny, cnt])
               
    return -1
cnt= 0
res = bfs()
print(res)