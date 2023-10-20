n = int(input())
dp = [float('inf')] * (n+1)

if n < 5: # 5키로 이하이면 3키로만 1출력하고 다른 무게는 -1
    print(1 if n == 3 else -1)

if n >= 5: # 5키로 이상이면 dp 진행
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n+1):
        dp[i] = min(dp[i-3], dp[i-5]) + 1 # 3/5키로 중 어떤 봉지를 선택해야 더 적은 봉지수인지
    print(dp[n] if dp[n] != float('inf') else -1)