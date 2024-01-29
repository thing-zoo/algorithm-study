n = int(input())
p = list(map(int, input().split()))
dp = [0]*(n+1) # dp[i] = i개의 팩을 사는데 최대값
dp[1] = p[0]
for i in range(2, n+1):
    dp[i] = p[i-1]
    for j in range(1, i//2+1): # i개의 팩을 사는 경우의 수
        dp[i] = max(dp[i], dp[i-j]+dp[j]) # 현재값과 i-j짜리팩과 j짜리팩을 사는 값 비교
print(dp[n])