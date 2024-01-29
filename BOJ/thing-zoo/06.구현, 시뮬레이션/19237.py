dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, k = map(int, input().split())
smell = [[[0,0] for _ in range(n)] for _ in range(n)] # smell[x][y] = [상어번호, 남은시간]
data = [list(map(int, input().split())) for _ in range(n)] # data[x][y] = 상어 번호(1~) -> 현재 상어 위치
shark = [-1] + list(map(lambda x: int(x)-1, input().split())) # shark[n] = 현재 방향(0~3)
priority = [[]] + [[list(map(lambda x: int(x)-1, input().split())) for _ in range(4)] for _ in range(m)] # priority[n][d]

def move(): # 이동한 위치에 냄새뿌리고 기존 냄새 감소
    for x in range(n):
        for y in range(n):
            if smell[x][y][1] > 0: # 냄새가 있으면
                smell[x][y][1] -= 1 # 감소
            if data[x][y] != 0: # 상어가 있으면
                smell[x][y] = [data[x][y], k] # 냄새 뿌리기

def find(): # 이동할 위치 찾기
    new_data = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] == 0: continue # 상어가 없으면 넘기기

            now = data[x][y]
            d = shark[now]

            candi = []
			
            # 냄새 없는 칸 찾기
            for i in priority[now][d]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if smell[nx][ny][1] == 0:  # 냄새가 없으면
                    candi.append((nx, ny, i))
                    break

            if not candi: # 전부 냄새가 있음
                candi = []
                for i in priority[now][d]: # 우선순위대로
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if smell[nx][ny][0] == now:  # 자기 냄새인 걸로
                        candi.append((nx, ny, i))

            nx, ny, d = candi[0] # 젤 처음걸로
            if (new_data[nx][ny] == 0) or (now < new_data[nx][ny]): # 한칸에 가장 작은 번호만 남기기
                new_data[nx][ny] = now # 새로운 위치 저장
                shark[now] = d  # 현재 방향 저장
    return new_data

def check():
    candi = []
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                candi.append(data[x][y])
    return len(candi) == 1

answer = 0 # 1번 상어만 남기까지 걸린 시간
while True:
    # 이동
    move()
    data = find()
    answer += 1 # 시간 증가

    if check(): # 1번 상어만 남으면 종료
        break

    if answer >= 1000: # 1000초 넘어도 끝나지 않으면
        answer = -1
        break
print(answer)