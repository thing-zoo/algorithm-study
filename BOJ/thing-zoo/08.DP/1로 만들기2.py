n = int(input())
dp = [0]*(n+1)
path = [0]*(n+1)
dp[1] = 0; path[1] = 0
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    path[i] = i-1
    if i%3 == 0:
        if dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
            path[i] = i//3
    if i%2 == 0:
        if dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1
            path[i] = i//2
print(dp[n])
i = n
print(n, end=" ")
while path[i] != 0:
    print(path[i], end=" ")
    i = path[i]