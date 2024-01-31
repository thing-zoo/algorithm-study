# dp[i][j] = 동쪽 i개중에서 서쪽과 연결할 j개를 고르는 조합의 수
# 조합성질 이용: C(i,j) = C(i-1,j-1) + C(i-1, j)
dp = [[0]*30 for _ in range(30)]
dp[0][0] = 1
for i in range(1, 30):
    dp[i][0] = 1
    for j in range(1, 30):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[m][n])