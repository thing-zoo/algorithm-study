# dp[i]=ikg일때 필요한 최소 봉지 수
dp = [1e9]*5001 # 불가능한 경우 무한대
dp[0], dp[3] = 0, 1 # 계산을 위해 0은 0
n = int(input())
for i in range(5, n+1):
    # 3kg 봉지 쓰는 경우, 5kg 봉지 쓰는 경우, 둘다 못쓰는 경우(기존값:무한대)
    # 중 최소값을 택
    dp[i] = min(dp[i-3]+1, dp[i-5]+1, dp[i])
if dp[n] == 1e9:
    print(-1)
else:
    print(dp[n])