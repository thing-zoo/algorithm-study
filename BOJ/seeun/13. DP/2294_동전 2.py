import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [float('inf')] * (100000+1) # 동전의 가치가 100,000까지 가능하므로 배열 크기 설정
for c in coin:
    dp[c] = 1

for i in range(1, k+1):
    tmp = float('inf')
    for c in coin:
        if i > c:
            tmp = min(dp[i-c]+1, tmp) 
    dp[i] = min(tmp, dp[i])

print(dp[k] if dp[k] != float('inf') else -1)