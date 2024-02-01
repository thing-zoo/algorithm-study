# dp[i]=i를 만드는 데 필요한 제곱수의 최소 개수
dp = [1e9]*50001 # 무한대로 초기화
dp[0] = 0
for i in range(1, 50001):
    j = 1
    while j*j <= i: # i이하의 모든 제곱수에 대해
        dp[i] = min(dp[i-j*j]+1, dp[i])
        j += 1
n = int(input())
print(dp[n])