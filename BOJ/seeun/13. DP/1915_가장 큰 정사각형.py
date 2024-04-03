n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

length = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            if i > 0 and j > 0 and board[i][j-1] == board[i-1][j] == board[i-1][j-1] == '1': # 인접한 3개 칸이 모두 1이면
                dp[i][j] = min([dp[i][j-1], dp[i-1][j], dp[i-1][j-1]]) + 1 # 그중 가장 작은 정사각형 변 길이 +1
            else:
                dp[i][j] = 1 # 인접한 3칸으로 정사각형을 만들 수 없으면 혼자 정사각형
    length = max(length, max(dp[i]))

print(length*length)