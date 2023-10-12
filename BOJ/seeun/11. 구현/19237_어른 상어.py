N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shark_dir = [0]
shark_dir.extend(list(map(int, input().split()))) # i상어의 방향
priority = [] # i번 상어의 보는 방향에 따른 우선순위 저장

priority.append([])
for i in range(M):
    tmp = []
    for _ in range(4):
        t = list(map(int, input().split()))
        tmp.append(t)
    priority.append(tmp) # 


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
scent = [[[0, 0] for _ in range(N)] for _ in range(N)] # [상어번호, 남은 시간] k번
def remain_scent():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0: # 상어가 있으면
                scent[i][j] = [board[i][j], k]

def remove_scent(): # 시간 지날 때 마다 냄새 지우기 + 상어 마리수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                cnt += 1
            if scent[i][j][1] > 0:
                scent[i][j][1] -= 1
            if scent[i][j][1] == 0: # 남은냄새가 없으면 초기화
                scent[i][j] = [0, 0]

    return cnt

def move_shark():
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0: # 상어가 있으면
                num = board[i][j] # 상어 번호 구함
                candi = [] # 냄새가 없는 곳 중에 갈 수 있는 곳
                my = [] # 내 냄새가 있는 곳
                dir = shark_dir[num] # 현재 i상어가 보고 있는 방향
                pri = priority[num][dir-1] # i가 dir방향을 보고 있을 때 탐색 순서

                for p in pri: # p방향 탐색
                    nx = i + dx[p]
                    ny = j + dy[p]
                    if 0 <= nx < N and 0 <= ny < N: # 범위 내일 때
                        if scent[nx][ny][0] == num: # 해당 위치에 있는 냄새가 내거이면
                            my.append(p)
                        elif scent[nx][ny][1] == 0: # 해당 위치의 냄새가 0일 때
                            candi.append(p)

                if not candi: # 주변에 냄새가 없는 곳이 없으면
                    dir = my[0] # 내 냄새가 나는 곳으로 감
                else: # 빈칸이 있으면
                    dir = candi[0] # 우선순위 제일 높은 곳으로 감

                # 방향 수정, 위치 이동
                shark_dir[num] = dir
                nx, ny = i + dx[dir], j + dy[dir]
                if 0 <= nx < N and 0 <= ny < N:
                    if new_board[nx][ny] > 0: # 상어가 있으면
                        new_board[nx][ny] = min(new_board[nx][ny], num) # 상어 이동
                    else:
                        new_board[nx][ny] = num
    return new_board

times = 1
sharks = 0
remain_scent()

while times <= 1001:
    board = move_shark()
    sharks = remove_scent()
    remain_scent()
    if sharks == 1:
        break
    times += 1

if times > 1000:
    print(-1)
else:
    print(times)