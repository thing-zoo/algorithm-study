n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0]*k # dp[i] = i원을 만드는 경우의 수
for i in range(1, n+1): # 순서대로
    for j in range(coins[i-1], k+1, 1): # k원까지
        dp[j] += dp[j-coins[i-1]] # 경우 누적
print(dp[k])