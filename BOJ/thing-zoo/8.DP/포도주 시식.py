n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0]*(n+1)
if n < 3:
    print(sum(wine))
else:
    dp[1], dp[2] = wine[1], wine[1] + wine[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], max(dp[i-3] + wine[i-1], dp[i-2]) + wine[i])
    print(dp[n])