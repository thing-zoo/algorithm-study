from collections import deque
N, M, K = map(int, input().split())
ball = deque()
ballcnt = 0
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c].append([m, s, d, 1]) # 질량, 속도, 방향, 파이어볼 개수

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def move():
    global aftermove

    for i in range(N):
        for j in range(N):
            if board[i][j]: # 파이어볼이 있으면
                if board[i][j][0][3] == 4: # 4개 있을 때 각 방향으로 이동
                    m, s, d, _ = board[i][j][0]
                    for k in range(d, 8, 2):  # 홀/짝 방향으로 퍼뜨리기
                        nx = (i + dx[k] * s) % N
                        ny = (j + dy[k] * s) % N
                        aftermove[nx][ny].append([m, s, k, 1])
                else: # 한개만 있을 때
                    m, s, d, _ = board[i][j][0]
                    nx = (i + dx[d] * s) % N
                    ny = (j + dy[d] * s) % N
                    aftermove[nx][ny].append([m, s, d, 1])  # 이동한 위치에 파이어볼 저장

# 여러개인 곳 합치기
def union(board):
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1: # 파이어볼이 여러개인 곳이라면
                new_m = 0
                new_s = 0
                new_d = []

                # 질량, 속도, 방향을 공식에 따라 계산
                for b in board[i][j]:
                    new_m += b[0]
                    new_s += b[1]
                    new_d.append(b[2] % 2)

                new_m //= 5
                new_s //= len(board[i][j])
                
                # 질량이 없는 볼은 소멸됨
                if new_m == 0: 
                    board[i][j] = []
                    continue

                # 방향 결정 후 저장
                # [새로운질량, 새로운속도, 새로운방향의 시작점(0 or 1), 파이어볼 개수]
                if new_d.count(1) == 0 or new_d.count(0) == 0: # 모두 짝/홀수인 경우
                    board[i][j] = [[new_m, new_s, 0, 4]] 
                    new_d = 0
                else: # 짝/홀수가 섞여있는 경우
                    board[i][j] = [[new_m, new_s, 1, 4]]
                    new_d = 1


# k번 이동하기
for _ in range(K):
    aftermove = [[[] for _ in range(N)] for _ in range(N)]

    # aftermove에 다 옮기기
    move()

    # 중복인거 합쳐서 4개로 나눔
    union(aftermove)

    # 옮긴 후 보드를 기본 보드로 복사
    for i in range(N):
        board[i] = aftermove[i]

ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            ans += board[i][j][0][0]*board[i][j][0][3] # 파이어볼 질량 * 해당 위치의 파이어볼 개수
print(ans)