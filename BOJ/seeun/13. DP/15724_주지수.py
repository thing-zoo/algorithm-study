import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [[0 for _ in range(m+1)]]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

# 누적합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        board[i][j] += board[i][j-1]
for i in range(2, n+1):
    for j in range(1, m+1):
        board[i][j] += board[i-1][j]

# 범위 인구 출력
k = int(input())
for _ in range(k):
    a, b, x, y = map(int, input().split())
    ans = 0
    ans = board[x][y] - board[a-1][y] - board[x][b-1] + board[a-1][b-1]
    print(ans)