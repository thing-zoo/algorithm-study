n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
# dp[i][j] = i까지 j번 제거했을 때 최장짝수연속부분수열의 길이
dp = [[0]*(k+1) for _ in range(n+1)]
answer = 0
for i in range(1, n+1):
    for j in range(k+1):
        if s[i]%2 == 0: # 짝수인 경우 s[i]포함 가능
            # 이번에 제거 안해도 됨
            # 이전 수열에서 j번 제거한 길이 + 1
            dp[i][j] = max(dp[i-1][j] + 1, dp[i][j])
        elif j > 0 and s[i]%2: # 홀수인 경우 s[i]포함 불가
            # 이번에 제거해야 함
            # 이전 수열에서 j-1번 제거한 길이
            dp[i][j] = max(dp[i-1][j-1], dp[i][j])
    answer = max(answer, max(dp[i]))
print(answer)