n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
if n < 2:
    print(scores[1])
else:
    dp = [[0]*2 for _ in range(n+1)]
    dp[1][0] = scores[1]
    dp[2][0] = scores[1] + scores[2]
    dp[2][1] = scores[2]
    for i in range(3, n+1):
        # dp[i][0] = 1칸으로 i에 오른 경우
        dp[i][0] = dp[i-1][1] + scores[i]
        # dp[i][1] = 2칸으로 i에 오른 경우
        dp[i][1] = max(dp[i-2]) + scores[i]
    print(max(dp[n]))