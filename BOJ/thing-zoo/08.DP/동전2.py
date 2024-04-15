# 분할할 수 없는 배낭문제
n, k = map(int, input().split())
coins = list(set([int(input()) for _ in range(n)]))
# dp[i] = i원를 만드는 동전 개수의 최솟값
dp = [1e9]*(k+1)
dp[0] = 0
for i in range(len(coins)):
    for j in range(coins[i], k+1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)
print(dp[k] if dp[k] != 1e9 else -1)