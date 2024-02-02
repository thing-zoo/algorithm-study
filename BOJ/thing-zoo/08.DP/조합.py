# 조합 성질 이용
n, m = map(int, input().split())
dp = [[0]*101 for _ in range(101)]
dp[0][0] = 1 # C(n,n)=1
for i in range(1, 101):
    dp[i][0] = 1 # C(n,0)=1
    for j in range(1, i+1):
        # C(n,m) = C(n-1,m-1) + C(n-1, m)
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[n][m])