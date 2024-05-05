def check(x, y):
    count1, count2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0: # 짝짝이거나 홀홀일때
                if board[x+i][y+j] != 'W':
                    count1 += 1
                if board[x+i][y+j] != 'B':
                    count2 += 1
            else:
                if board[x+i][y+j] != 'B':
                    count1 += 1
                if board[x+i][y+j] != 'W':
                    count2 += 1
    return min(count1, count2)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
answer = 1e9
for i in range(n):
    for j in range(m):
        if i + 8 <= n and j + 8 <= m:
            answer = min(answer, check(i, j))
print(answer)