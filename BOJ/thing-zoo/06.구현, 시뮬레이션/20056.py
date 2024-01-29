import copy
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
board = [[[] for _ in range(N)] for _ in range(N)]

# 파이어볼 초기화
for i in range(M):
    r, c, m, s, d = fireball[i]
    board[r-1][c-1].append([m, s, d])

# 이동 시작
for _ in range(K): # k번 이동
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while board[i][j]:
                m, s, d = board[i][j].pop()

                # 1번과 n번이 연결되어있음
                nr = (i + dr[d]*s)%N
                nc = (j + dc[d]*s)%N
                if (nr < 0 or nr > N-1) or (nc < 0 or nc > N-1): # 범위 밖일 경우
                    continue
                new_board[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(new_board[i][j]) >= 2: # 파이어볼이 2개 이상이면
                m = s = 0
                flag = True # 모두 홀수거나 모두 짝수인 경우
                for k in range(len(new_board[i][j])):
                    m += new_board[i][j][k][0]
                    s += new_board[i][j][k][1]
                    if k > 0 and (new_board[i][j][k-1][2]%2==0) != (new_board[i][j][k][2]%2==0): # 홀짝일 경우
                        flag = False
                m = int(m/5)
                s = int(s/len(new_board[i][j]))
                new_board[i][j].clear()

                if m == 0: continue
                for k in range(4):
                    if flag: d = k*2
                    else: d = k*2+1
                    new_board[i][j].append([m, s, d])
    board = copy.deepcopy(new_board)

# 질량 세기
result = 0
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            result += board[i][j][k][0]
print(result)