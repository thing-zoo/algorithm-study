n = int(input())
board = [input() for _ in range(n)]
x = y = -1
waist_x = -1
left_arm = right_arm = waist = left_leg = right_leg = 0

flag = False
for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            x = i + 1
            y = j
            flag = True
    if flag: break

for j in range(y-1, -1, -1):
    if board[x][j] == '*':
        left_arm += 1

for j in range(y+1, n):
    if board[x][j] == '*':
        right_arm += 1

for i in range(x+1, n):
    if board[i][y] == '*':
        waist += 1
        waist_x = i

for i in range(waist_x+1, n):
    if board[i][y-1] == '*':
        left_leg += 1

for i in range(waist_x+1, n):
    if board[i][y+1] == '*':
        right_leg += 1

print(x+1, y+1, sep=' ')
print(left_arm, right_arm, waist, left_leg, right_leg, sep=' ')