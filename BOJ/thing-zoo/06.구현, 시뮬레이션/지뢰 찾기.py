def count_bomb(x, y):
    dx = (-1, -1, 0, 1, 1, 1, 0, -1)
    dy = (0, 1, 1, 1, 0, -1, -1, -1)
    result = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if board[nx][ny] == '*':
            result += 1
    return result

n = int(input())
board = []
bomb = set()
for i in range(n):
    board.append(input())
    for j in range(n):
        if board[i][j] == '*':
            bomb.add((i,j))

flag = False
answer = [[-1]*n for _ in range(n)] 
# -1: 온점, -2: 폭탄
for i in range(n):
    temp = input()
    for j in range(n):
        if temp[j] == 'x':
            if board[i][j] == '*':
                flag = True
            else:
                answer[i][j] = count_bomb(i, j)

if flag:
    for i, j in bomb:
        answer[i][j] = -2

for i in range(n):
    for j in range(n):
        if answer[i][j] == -1:
            print('.', end='')
        elif answer[i][j] == -2:
            print('*', end='')
        else:
            print(answer[i][j], end='')
    print()