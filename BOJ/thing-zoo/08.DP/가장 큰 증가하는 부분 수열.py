n = int(input())
data = list(map(int, input().split()))
dp = [0]*n
dp[0] = data[0]
max_sum = dp[0]
for i in range(1, n):
    dp[i] = data[i]
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+data[i])
    max_sum = max(dp[i], max_sum)
print(max_sum)