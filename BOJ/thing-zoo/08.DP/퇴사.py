n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*n
profit = 0
if data[0][0] <= n:
    dp[0] = data[0][1]
    profit = dp[0]
for i in range(1, n):
    if i + data[i][0] > n:
        continue
    dp[i] = data[i][1]
    for j in range(i):
        if j + data[j][0] >= i + 1:
            continue
        dp[i] = max(dp[i], dp[j]+data[i][1])
    profit = max(profit, dp[i])
print(profit)