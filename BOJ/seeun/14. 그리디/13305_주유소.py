import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

minlist = [0] * n # 각 도시까지 중 최저가 저장
mincost = cost[0] # 현재까지 최저가

for i in range(n):
    if cost[i] < mincost: # 현재 도시 주유소 가격이 더 저렴하면 최저가 갱신
        mincost = cost[i]
    minlist[i] = mincost # 0~i도시까지 최저가 가격 저장

ans = 0
for i in range(n-1):
    ans += dist[i] * minlist[i] # 최저가 기름값 * 거리
print(ans)