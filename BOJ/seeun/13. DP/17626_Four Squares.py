import math
n = int(input())
dp = [float('inf')] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i-j*j]+dp[j*j])

print(dp[-1])