dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def spread():
    global room
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if room[i][j]>0: # 먼지가 있으면
                monji = room[i][j]//5
                cnt = 0 # 몇 방향으로 퍼져나갔는지  
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0  <= nj < m and room[ni][nj] != -1: # 범위 내 & 공기 청정기 아니면 퍼져나감
                        tmp[ni][nj] += monji
                        cnt += 1
                tmp[i][j] += room[i][j]-monji*cnt
    room = tmp
    return

def air():
    global room
    # 공기 청정기 윗부분
    x, y = machine[0]
    for i in range(x-1, 0, -1):
        room[i][0] = room[i-1][0]
    for j in range(0, m-1):
        room[0][j] = room[0][j+1]
    for i in range(0, x):
        room[i][m-1] = room[i+1][m-1]
    for j in range(m-1, 1, -1):
        room[x][j] = room[x][j-1]
    room[x][y+1] = 0
    room[x][y] = -1

    # 공기 청정기 아랫부분
    x, y = machine[1]
    for i in range(x+1, n-1):
        room[i][0] = room[i+1][0]
    for j in range(0, m-1):
        room[n-1][j] = room[n-1][j+1]
    for i in range(n-1, x, -1):
        room[i][m-1] = room[i-1][m-1]
    for j in range(m-1, 1, -1):
        room[x][j] = room[x][j-1]
    room[x][y+1] = 0
    room[x][y] = -1
    return

# main
n, m, t = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 공기 청정기 위치 저장
machine = []
for i in range(n):
   if room[i][0] == -1:
       machine.append([i, 0])
       machine.append([i+1, 0])
       break
    
# t번 반복
# 미세먼지 확산 (새로운 배열에)
# 공기이동
for _ in range(t):
    spread()
    air()

res = 0
for i in range(n):
    for j in range(m):
        if room[i][j] != -1:
            res += room[i][j]
print(res)