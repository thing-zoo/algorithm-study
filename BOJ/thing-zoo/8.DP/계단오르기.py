n = int(input())
data = [0] + [int(input()) for _ in range(n)]
if n == 1: 
    print(data[1])
else:
    dp = [[0]*(n+1) for _ in range(3)]
    dp[1][1] = data[1]
    dp[1][2] = data[1] + data[2]; dp[2][2] = data[2]
    for i in range(3, n+1):
        dp[1][i] = dp[2][i-1] + data[i]
        dp[2][i] = max(dp[1][i-2], dp[2][i-2]) + data[i]
    print(max(dp[1][n], dp[2][n]))