n, m, x, y, cmd_n = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
cmdlist = list(map(int, input().split()))

dice = [[0 for _ in range(3)] for _ in range(4)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(cmd_n):
    cmd = cmdlist[i]
    if x + dx[cmd-1] < 0 or x + dx[cmd-1] >= n or y + dy[cmd-1] < 0 or y + dy[cmd-1] >= m:
        continue
    x += dx[cmd-1]
    y += dy[cmd-1]
    if cmd == 1: # 동쪽으로 굴리기
        tmp = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = tmp
        
    elif cmd == 2:
        tmp = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = tmp
        
    elif cmd == 3:
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp

    elif cmd == 4:
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = tmp
        
    
    if board[x][y] == 0:
            board[x][y] = dice[3][1]
    else:
        dice[3][1] = board[x][y]
        board[x][y] = 0
    # for i in range(4):
    #         print(dice[i], board[i])
    # print()
    print(dice[1][1])
   
