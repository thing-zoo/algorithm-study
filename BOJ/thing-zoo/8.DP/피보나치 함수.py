import sys
input = sys.stdin.readline
dp = [[0]*41 for _ in range(2)]
dp[0][0], dp[1][0] = 1, 0
dp[0][1], dp[1][1] = 0, 1
for i in range(2, 41):
    dp[0][i] = dp[0][i-1] + dp[0][i-2]
    dp[1][i] = dp[1][i-1] + dp[1][i-2]
t = int(input())
for _ in range(t):
    n = int(input())
    sys.stdout.write("%d %d\n" %(dp[0][n], dp[1][n]))