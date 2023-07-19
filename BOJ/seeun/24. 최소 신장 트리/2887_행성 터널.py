from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
planets = []
conn = [False] * n
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append([x, y, z, i])

xsort = sorted(planets, key=lambda x:x[0]) # x좌표 기준 오름차순으로 정렬 => 작은 좌표부터 가까이 있는 점들 순서대로 정렬됨
ysort = sorted(planets, key=lambda x:x[1])
zsort = sorted(planets, key=lambda x:x[2])

hq = []
edge = [[] for _ in range(n)] # i행성에서 갈 수 있는 행성들과 거리를 x, y, z 기준으로 하나씩 저장함
for i in range(n-1):
    x, y, z, p1 = xsort[i]
    a, b, c, p2 = xsort[i+1]
    edge[p2].append([abs(x-a), p1]) # p2에서 p1을 가는데 드는 비용(x좌표 기준): abs(x-a)
    edge[p1].append([abs(x-a), p2])

    x, y, z, p1 = ysort[i]
    a, b, c, p2 = ysort[i+1]
    edge[p2].append([abs(y-b), p1])
    edge[p1].append([abs(y-b), p2])

    x, y, z, p1 = zsort[i]
    a, b, c, p2 = zsort[i+1]
    edge[p2].append([abs(z-c), p1])
    edge[p1].append([abs(z-c), p2])
    
print(hq)
ans = 0
heappush(hq, [0, 0]) # 0번째 행성에서 시작
while hq:
    cost, p = heappop(hq)
    if conn[p]:
        continue
    conn[p] = True
    ans += cost
    for i in edge[p]: # p에서 갈 수 있는 행성들의 거리를 힙에 넣음
        heappush(hq, [i[0], i[1]]) # [거리, 행성번호]
print(ans)