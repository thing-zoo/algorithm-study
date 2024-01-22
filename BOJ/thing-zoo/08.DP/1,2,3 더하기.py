t = int(input())
data = [int(input()) for _ in range(t)]
n = max(data)
dp = [0]*(n+1)
dp[1] = 1; dp[2] = 2; dp[3] = 4
for i in range(4, n+1):
    if i - 1: dp[i] += dp[i-1]
    if i - 2: dp[i] += dp[i-2]
    if i - 3: dp[i] += dp[i-3]
for x in data:
    print(dp[x])