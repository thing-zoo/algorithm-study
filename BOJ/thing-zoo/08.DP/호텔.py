# 분할 할 수 없는 배낭 문제
c, n = map(int, input().split()) # 목표 고객수, 도시 수
dp = [1e9]*(c+100) # dp[i] = i명일 때 최소 홍보비용
dp[0] = 0
for _ in range(n):
    cost, people = map(int, input().split())
    for i in range(people, c+100):
        dp[i] = min(dp[i], dp[i-people] + cost)
print(min(dp[c:])) # 적어도 c명일 때 최소 비용이므로