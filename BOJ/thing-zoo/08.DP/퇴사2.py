import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1) # dp[i] = i번째날의 최대 수익
for i in range(n):
    time, profit = map(int, input().rstrip().split())
    if i + time <= n: # 상담이 n일안에 가능하면 상담 진행
        dp[i + time] = max(dp[i + time], dp[i] + profit) # 상담마친 날의 수익과 이번상담을 했을때까지의 수익 비교
    # 상담을 진행하지 않을 경우
    dp[i + 1] = max(dp[i + 1], dp[i]) # 다음날의 수익과 현재까지의 수익 비교
print(dp[n])