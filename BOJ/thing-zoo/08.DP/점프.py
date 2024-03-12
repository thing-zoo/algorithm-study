n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)] # dp[i][j] = 현위치까지 이동할 수 있는 경로의 개수
dp[0][0] = 1 # 첫 시작점
for i in range(n):
    for j in range(n):
        if i == j == n-1: break # 도착하면 종료
        jump = board[i][j]
        if i + jump < n:
            dp[i + jump][j] += dp[i][j]
        if j + jump < n:
            dp[i][j + jump] += dp[i][j]
print(dp[n-1][n-1])