n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [0] + [1]*9
for i in range(1, n):
    for j in range(10):
        if dp[i-1][j]:
            if j != 0:
                dp[i][j-1] += dp[i-1][j]%1000000000
            if j != 9:
                dp[i][j+1] += dp[i-1][j]%1000000000
print(sum(dp[n-1])%1000000000)