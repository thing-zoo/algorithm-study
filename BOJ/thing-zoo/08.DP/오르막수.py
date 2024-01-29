n = int(input())
dp = [[0]*10 for _ in range(n+1)] # dp[i][j] = 길이가 i이고 일의 자리가 j인 수의 개수
dp[1] = [1]*10
for i in range(2, n+1): # 길이 i일때
    for j in range(10): # 일의자리 j의 개수는
        for k in range(j+1): # i-1의 일의 자리 0...j 값을 더해주면됨
            dp[i][j] = (dp[i][j] + dp[i-1][k])%10007
print(sum(dp[n])%10007)