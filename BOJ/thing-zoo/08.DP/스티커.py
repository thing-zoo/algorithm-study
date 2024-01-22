t = int(input())
for _ in range(t):
    n = int(input())
    dp = [ [0]+list(map(int, input().split())) for _ in range(2) ] # dp[i][j] = (i,j)번째 스티커를 포함하는 최대값
    for j in range(2, n+1):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][n], dp[1][n]))