n = int(input())
a, b = [0]*n, [0]*n
a_b, b_a = [0]*(n-1), [0]*(n-1)
dp = [[0]*2 for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    a[i], b[i] = temp[0], temp[1]
    if i != n-1: a_b[i], b_a[i] = temp[2], temp[3]
dp[0][0], dp[0][1] = a[0], b[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0] + a[i], dp[i-1][1] + b_a[i-1] + a[i])
    dp[i][1] = min(dp[i-1][1] + b[i], dp[i-1][0] + a_b[i-1] + b[i])
print(min(dp[n-1]))