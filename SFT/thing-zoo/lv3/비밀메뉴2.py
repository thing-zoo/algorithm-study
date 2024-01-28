n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0 # 최장 공통 부분 수열의 길이
# dp[i][j]: a[i]와 b[j]까지 보았을 때의 최장 공통 부분 수열의 길이
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        answer = max(answer, dp[i][j])
print(answer)