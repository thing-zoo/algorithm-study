N, M = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(N)]
cloud = [[0]*N for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

# 초기 구름 저장
cloud[N-1][0] = 1
cloud[N-1][1] = 1
cloud[N-2][0] = 1
cloud[N-2][1] = 1

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def flow(d, s): # 구름 움직이기
    moved_cloud=[[0] * N for _ in range(N)]
    copylist = [] # 물복사 버그를 적용할 위치 저장
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1: # 구름이 있으면
                # 이동할 위치 계산
                nx = (i+dx[d]*s) % N
                ny = (j+dy[d]*s) % N
                moved_cloud[nx][ny] = 1 # 새로운 자리로 구름 이동
                water[nx][ny] += 1 # 이동한 자리에서 비 내리기
                copylist.append([nx, ny]) # 비 온 곳은 물복사버그 써야함

    # 물복사 버그 마법 적용
    water_copy(copylist) 
    return moved_cloud # 이동한 구름

def make(old_cloud): # 구름 만들기
    cloud = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if water[i][j] >= 2 and not old_cloud[i][j]: # 물이 2 이상이고 이전에 구름이 있었던 칸이 아니면
                cloud[i][j] = 1
                water[i][j] -= 2
    
    return cloud

def water_copy(copylist): # 물복사 버그
    for x, y in copylist:
        cnt = 0
        for i in range(2, 9, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < N: # 대각선이 범위 내이면
                if water[nx][ny] > 0: # 물이 있으면 카운트 +1
                    cnt += 1

        water[x][y] += cnt

for i in range(M):
    moved_cloud = flow(move[i][0], move[i][1]) # 이전에 구름이 있었던 위치 받아옴
    cloud = make(moved_cloud) # 이전에 구름이 있었던 곳 제외하고 새로운 구름 생성
    
# 물 양 계산
ans = 0
for i in range(N):
    ans += sum(water[i])

print(ans)