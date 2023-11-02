import sys
n = int(input())
stone = list(map(int, input().split()))

# dp[i]: i에 무조건 도착해야할 때 그전까지 밟을 수 있는 돌의 최대 개수
dp = [1] * n # 자기자신은 밟을 수 있으니까 1로 초기화

for i in range(1, n):
  tmp = 0 # 지금까지 밟은 돌의 개수
  for j in range(i):
    if stone[i] > stone[j]: # j가 i보다 작으면 밟을 수 있음
      tmp = max(tmp, dp[j]) # 지금까지 밟은돌 vs j까지 가는데 밟을 수 있는 최대 돌
  dp[i] = tmp + 1 # 지금까지 밟은 돌 + i번 돌

print(max(dp))