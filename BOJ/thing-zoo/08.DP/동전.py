# 분할할 수 없는 배낭문제
t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    # dp[i] = i원을 만드는 경우의 수
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], m+1):
            dp[j] += dp[j-coins[i]]
    print(dp[m])