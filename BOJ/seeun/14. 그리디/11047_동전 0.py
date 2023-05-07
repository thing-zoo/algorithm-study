n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

res = 0
# 동전이 배수관계에 있기 때문에 가능한 방법
for i in range(n-1, -1, -1):
    res += k//coins[i] # 가장 큰 돈을 가능한 많이 넣기
    k %= coins[i] # 남은돈으로 변경
print(res)