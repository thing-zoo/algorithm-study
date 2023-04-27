n = int(input())
data = list(map(int, input().split()))
dp = [1]*n
max_length = 1
for i in range(1, n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
    max_length = max(max_length, dp[i])
print(max_length)