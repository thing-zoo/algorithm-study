r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
island_x = []
island_y = []
flood = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            count = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni >= r or nj < 0 or nj >= c:
                    count += 1
                elif board[ni][nj] == '.':
                    count += 1
            if count >= 3:
                flood.append((i,j))
            else:
                island_x.append(i)
                island_y.append(j)
for i, j in flood:
    board[i][j] = '.'
for i in range(min(island_x), max(island_x)+1):
    for j in range(min(island_y), max(island_y)+1):
        print(board[i][j], end='')
    print()