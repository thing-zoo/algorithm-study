n = int(input())
dp = [0]*n
dp[0] = 9
count = [0]+[1]*9
for i in range(1, n):
    dp[i] = dp[i-1]*2 - (count[0]+count[9])
    new_count = [0]*10
    for j in range(10):
        if j - 1 >= 0:
            new_count[j - 1] += count[j]
        if j + 1 < 10:
            new_count[j + 1] += count[j]
    count = new_count[:]
print(dp[n-1]%10**9)