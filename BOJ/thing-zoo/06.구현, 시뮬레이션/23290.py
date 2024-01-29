MAX_SIZE = 4
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
m, s = map(int, input().split()) # 물고기 수, 마법연습 횟수
smell = [[0]*(MAX_SIZE+1) for _ in range(MAX_SIZE+1)] # 냄새 남은시간
board = [[[] for _ in range(MAX_SIZE+1)] for _ in range(MAX_SIZE+1)] # 물고기 방향들
for i in range(1, m+1):
    x, y, d = map(int, input().split())
    board[x][y].append(d-1) # 방향(0~7)
shark = tuple(map(int, input().split())) # 상어 위치

def fish_move(): # 물고기 복제 후 이동
    new_board = [[[] for _ in range(MAX_SIZE + 1)] for _ in range(MAX_SIZE + 1)]
    for x in range(1, MAX_SIZE+1):
        for y in range(1, MAX_SIZE+1):
            for now in board[x][y]: # 물고기가 있으면
                moved = False
                d = now
                for i in range(8): # 8방향에 대해
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if (nx < 1 or nx > MAX_SIZE or ny < 1 or ny > MAX_SIZE) or ((nx, ny) == shark) or smell[nx][ny] > 0:
                        d = (8 + d - 1)%8 # 범위밖이거나 상어거나 냄새가 있으면 반시계 45도 회전
                        continue
                    moved = True
                    new_board[nx][ny].append(d) # 현재 방향 넣기
                    break
                if not moved: new_board[x][y].append(now) # 이동안하면 원래 방향 넣기
    return new_board

def shark_move(x, y, p, f, new_board): # 상어 이동(x, y, 이동좌표들, 물고기개수, new_board)
    global max_fish, shark, path
    if len(p) == 3: # 3칸까지만 이동
        if max_fish < f: # 물고기 개수가 많은걸로 갱신
            max_fish = f
            shark = (x, y)
            path = p
        return

    # 상 좌 하 우
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4): # dfs로 사전순 접근
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > MAX_SIZE or ny < 1 or ny > MAX_SIZE: continue
        if (nx, ny) not in p: # 방문 안한 곳일 경우 물고기 개수 추가
            shark_move(nx, ny, p + [(nx, ny)], f + len(new_board[nx][ny]), new_board)
        else: # 방문 한 곳일 경우 물고기 개수 추가 안함
            shark_move(nx, ny, p + [(nx, ny)], f, new_board)
def put_smell(path, new_board): # 냄새 뿌리기
    for x, y in path: # 상어 이동 경로에
        if new_board[x][y]: # 물고기가 있으면
            smell[x][y] = 2 # 냄새뿌리기(2번 이후 사라짐)
            new_board[x][y] = [] # 모든 물고기 제거

def remove_smell(): # 냄새 없애기
    for x in range(1, MAX_SIZE+1):
        for y in range(1, MAX_SIZE+1):
            if smell[x][y]:
                smell[x][y] -= 1
def duplicate(new_board): # 복제하기
    for x in range(1, MAX_SIZE+1):
        for y in range(1, MAX_SIZE+1):
            board[x][y] += new_board[x][y] # 기존상태에서 복제후 이동한 물고기 더하기

for _ in range(s):
    new_board = fish_move()
    max_fish = -1
    path = []
    shark_move(shark[0], shark[1], [], 0, new_board)
    remove_smell()
    put_smell(path, new_board)
    duplicate(new_board)

answer = 0 # 물고기 개수
for x in range(1, MAX_SIZE+1):
    for y in range(1, MAX_SIZE+1):
        answer += len(board[x][y])
print(answer)