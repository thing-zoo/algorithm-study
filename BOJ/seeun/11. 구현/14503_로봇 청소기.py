def cleaning(x, y, dir): #현재 위치, 내가바라보는 방향
    cleaned = [[0]*m for _ in range(n)]
    global res, cnt
    cnt = 0
    # 현재 칸이 청소되지 않았으면 현재칸 청소
    if cleaned[x][y] == 0 and room[x][y] == 0:
            cleaned[x][y] = 1 # 현재칸 청소
            res += 1
    # 주변 살피기
    while True: 
        flag = False
        for i in range(4):
            i = (dir+i+1)%4 # 현재 방향기준으로 반시계90도 회전 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < n-1 and 0 < ny < m-1:
                if room[nx][ny] == 0 and cleaned[nx][ny] == 0: # 벽이 아니고 청소안된 칸 있으면
                    res += 1
                    x = nx
                    y = ny
                    dir = i
                    cleaned[nx][ny] = 1
                    flag = True
                    break
        if not flag: # 하나도 청소 못했거나 벽이었으면 여기 걸림 -> 후진할겨
            x = x+backx[dir]
            y = y+backy[dir]
            if x <=0 or x>=n-1 or y<=0 or y>=m-1 or room[x][y] == 1:# 후진한게 벽이면 종료
                return 

n, m = map(int, input().split())
x, y, dir = map(int, input().split())
room = []
cleaned = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
backx = [1, 0, -1, 0]
backy = [0, 1, 0, -1]
res = 0

for _ in range(n):
    room.append(list(map(int, input().split())))

cleaning(x, y, (4-dir)%4)
print(res)