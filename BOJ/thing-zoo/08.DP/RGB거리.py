R,G,B = 0,1,2
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(3)]
dp[R][0] = cost[0][R]; dp[G][0] = cost[0][G]; dp[B][0] = cost[0][B]
for i in range(1, n):
    dp[R][i] = min(dp[G][i-1], dp[B][i-1]) + cost[i][R]
    dp[G][i] = min(dp[R][i-1], dp[B][i-1]) + cost[i][G]
    dp[B][i] = min(dp[R][i-1], dp[G][i-1]) + cost[i][B]
print(min(dp[R][n-1], dp[G][n-1], dp[B][n-1]))