n, k = map(int, input().split())
w, v = [], []
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a); v.append(b)

dp = [[0]*(k+1) for _ in range(n)] # dp[i][j]: 최대 무게가 j일때, i개의 아이템까지 봤을때 최대가치
for i in range(n): # 아이템을 순서대로
    for j in range(1, k+1): # k까지
        if j >= w[i]: # 포함할 수있으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i]) # 포함하지 않았을때 값과 포함했을때 비교
        else: # 포함할 수 없으면
            dp[i][j] = dp[i-1][j] # 그전 값 그대로
print(dp[n-1][k])