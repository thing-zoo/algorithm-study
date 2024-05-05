n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1]% 1000000007 + dp[i-2]% 1000000007) % 1000000007
    print(dp[n])