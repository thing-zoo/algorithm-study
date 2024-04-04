n = int(input()) # 돌의 개수
# i번째 돌에서 작은점프, 큰점프에 필요한 에너지
energy = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input()) # 매우 큰 점프에 필요한 에너지
# dp[i][j] = i번째 돌까지 가는데 필요한 최소 에너지(j: 매우큰점프 사용 유무)
dp = [[1e9]*2 for _ in range(n)]
dp[0] = [0, 1e9]
for i in range(n-1):
    dp[i+1][0] = min(dp[i+1][0], dp[i][0] + energy[i][0])
    dp[i+1][1] = min(dp[i+1][1], dp[i][1] + energy[i][0])
    if i+2 < n:
        dp[i+2][0] = min(dp[i+2][0], dp[i][0] + energy[i][1])
        dp[i+2][1] = min(dp[i+2][1], dp[i][1] + energy[i][1])
    if i+3 < n:
        dp[i+3][1] = min(dp[i+3][1], dp[i][0] + k)
print(min(dp[n-1]))