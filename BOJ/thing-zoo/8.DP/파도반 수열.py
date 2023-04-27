dp = [0]*101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1,1,1,2,2
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])