import copy
dx = [ -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(board, i): # i번 물고기의 위치 반환, 해당 물고기가 없으면 false
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == i:
                return [x, y]

def find_candi_loc(x, y, board): # 상어가 x, y, dir 일 때 갈 수 있는 위치 반환
    candi = []
    dir = board[x][y][1]
    for _ in range(1, 4): # 한 방향으로 최대 3칸 움직이기 가능
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= 4 or  y < 0 or y >= 4 or board[x][y][0] == -1: # 범위밖이거나 빈칸이면 못감
            continue
        candi.append([x, y])
    return candi

def move_fish(sx, sy, board): # 모든 물고기 한차례 이동
    for i in range(1, 17): # 번호 작은 물고기 순서대로
        pos = find_fish(board, i)
        if pos: # 살아있으면 위치 받아옴
            x, y = pos[0], pos[1]
            dir = board[x][y][1]

            for t in range(0, 8): # 8방향 확인
                d  = (dir + t) % 8
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: # 범위밖이거나
                    continue
                if nx == sx and ny == sy: # 상어가 있으면 못감
                    continue
    
                board[x][y][1] = d # 진행방향 바뀐거 체크
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                break

    return board


def move_shark(x, y, board, eat): # x, y위치에 있는 물고기를 먹고 시작
    global ans
    board = copy.deepcopy(board)
    eat += board[x][y][0] # 먹은 물고기 저장
    board[x][y][0] = -1 # 해당 위치의 물고기 먹기

    # 물고기 움직이기
    move_fish(x, y, board)

    # 물고기 이동 후 상어가 갈 수 있는 위치 구하기
    candi = find_candi_loc(x, y, board) 
    
    # 백트래킹 시작
    if candi:
        for nx, ny in candi:
            move_shark(nx, ny, board, eat) # 저 위치에 있는 물고기 먹으러 가기
    
    # 더이상 갈 수 있는 곳이 없으면 정답 갱신하고 종료
    else:
        ans = max(ans, eat)

        return

# 메인 -----------------------------------------
n = 4
board = [[0] * n for _ in range(n)]
for i in range(0, 4):
    tmp = list(map(int, input().split()))
    for j in range(0, 4):
        board[i][j] = [tmp[j*2], tmp[j*2+1]-1]

ans = 0 # 상어가 먹은 물고기 번호의 최대 합
move_shark(0, 0, board, 0)
print(ans)