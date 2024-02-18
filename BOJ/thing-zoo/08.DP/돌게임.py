# dp[i]=돌이 i개일때 게임 횟수
dp = [0]*1001
dp[1], dp[2] = 1, 2
for i in range(3, 1001):
    dp[i] = min(dp[i-1], dp[i-3]) + 1
n = int(input())
if dp[n]%2: # 게임횟수가 홀수면
    print('SK') # 항상 상근 승 
else:
    print('CY') # 항상 창영 승