# 좌~시계방향 0~7
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어의 방향: 상좌하우 1~4
sdx = [0, -1, 0, 1, 0]
sdy = [0, 0, -1, 0, 1]

def remove_scent(): # 냄새 없애기
    global scent
    for i in range(N):
        for j in range(N):
            if scent[i][j] > 0:
                scent[i][j] -= 1

def move_fish(sx, sy, old_board): # 물고기 움직이기
    old_board = [old_board[i][:] for i in range(N)]
    new_board = [[[] for _ in range(N)] for _ in range(N)] # 이동한 물고기 저장
    for x in range(N):
        for y in range(N):
            if len(old_board[x][y]) > 0: # 물고기가 있으면
                for dir in old_board[x][y]: # 해당 칸에 있는 물고기 모두 탐색
                    put = False # 탐색 단계에서 이동 했는지

                    for i in range(dir + 8, dir, -1): # 8방향 확인
                        nx = x + fdx[i%8]
                        ny = y + fdy[i%8]
                        if 0 <= nx < N and 0 <= ny < N:
                            if scent[nx][ny] == 0 and (nx != sx or ny != sy): # 냄새가 없고 상어가 없으면
                                new_board[nx][ny].append(i%8) # 이동한 위치 저장
                                put = True
                                break
                    # 한바퀴 탐색해도 갈 곳이 없으면 제자리에 머무르기
                    if not put:
                        new_board[x][y].append(dir)

    return new_board

def find_route(x, y, eat, move_list, old_board): # 숫자 상어위치, 없앤 물고기 수, 방향 순서, 보드
    global candi

    # 3칸을 지나왔으면
    if len(move_list) >= 3: 
        if candi[0] < eat: # 물고기를 더 많이 먹었으면 둘다 갱신
            candi[0] = eat
            candi[1] = move_list[:]
        elif candi[0] == eat: # 먹은 물고기가 같을 때
            if int(candi[1]) > int(move_list): # 이동 순서가 사전순으로 앞서는 것으로
                candi[1] = move_list
        return

    else:
        for i in range(1, 5): # 4방향 탐색
            board = [old_board[i][:] for i in range(N)] # 원본 보드 복제

            nx = x + sdx[i]
            ny = y + sdy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위 밖이면
                continue

            # 백트래킹 전
            if len(board[nx][ny]) > 0: # 물고기 있으면 냄새 남기고 잡아먹기, 상어이동
                eat += len(board[nx][ny])
                board[nx][ny] = []
            move_list += str(i) # 이동방향 저장
            find_route(nx, ny, eat, move_list, board)

            # 백트래킹 후 되돌려놓기
            if len(old_board[nx][ny]) > 0: # 물고기 있으면 냄새 남기고 없애기, 상어이동
                eat -= len(old_board[nx][ny]) # 먹은거 안먹은척
            move_list = move_list[:-1] # 방향 안갔다온척

def move_shark(route, old_board): # 구한 루트에 따라 상어 이동, 물고기 잡아먹기
    global sx, sy

    old_board = [old_board[i][:] for i in range(N)]
    for r in route:
        r = int(r)
        sx, sy = sx + sdx[r], sy + sdy[r]
        if len(old_board[sx][sy]) > 0: # 물고기 있으면 냄새 남기고 없애기, 상어이동
            scent[sx][sy] = 2
            old_board[sx][sy] = []
            sx, sy = sx, sy

    return old_board

def duplicate_fish(copy, origin): # copy에 있는 물고기들을 origin에 붙여넣기
    origin = [origin[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if copy[i][j]:
                origin[i][j].extend(copy[i][j])
    return origin

# =========================메인============================

N = 4
M, S = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
scent = [[0] * N for _ in range(N)]
for i in range(1, M+1):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    board[x][y].append(d)

sx, sy = map(int, input().split()) # 상어 위cl
sx -= 1
sy -= 1
ans = 0

# S번 반복
for _ in range(S):

    # 1. 물고기 복제 마법 -> copy_list에 일단 저장만
    copy_list = [board[i][:] for i in range(N)] # 첫 단계의 물고기 상태 저장해놓기
    
    # 2. 물고기이동
    candi = [0, "444"]
    after_move = move_fish(sx, sy, board) # 물고기 이동

    # 3. 물고기 이동 후 이전 단계에 생긴 냄새 없애기
    remove_scent()

    # 4. 백트래킹으로 상어가 이동할 루트 찾아내기
    find_route(sx, sy, 0, "", after_move) # 상어 이동할 방향 결정

    # 5. 상어 움직이기, 복제 마법 발현
    board = move_shark(candi[1], after_move)
    board = duplicate_fish(copy_list, board)

# 남은 물고기 마리 수 카운트
for i in range(N):
    for j in range(N):
        ans += len(board[i][j])

print(ans)