import sys
input = sys.stdin.readline
t = int(input())
dp = [0]*(10**6+1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 10**6+1):
    if i - 1: dp[i] += dp[i-1]
    if i - 2: dp[i] += dp[i-2]
    if i - 3: dp[i] += dp[i-3]
    dp[i] %= (10**9+9)
for _ in range(t):
    n = int(input().rstrip())
    sys.stdout.write("%d\n" %dp[n])