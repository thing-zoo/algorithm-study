from itertools import combinations

n, m = map(int, input().split())
town = []
house = []
chicken = []
for _ in range(n):
    town.append(list(map(int, input().split())))

# 집, 치킨집 위치 저장하기
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            house.append([i, j])
        elif town[i][j] == 2:
            chicken.append([i, j])

res = 99999999999
for i in range(1,  m+1): # 몇개 남길지 (최대 m개)
    for remain in combinations(chicken, i): # 지금 존재하는치킨집 중에 남길거 i개 고름
        tmp = 0 # 치킨거리 임시 저장변수
        for h in house:
            minDist = 999999999
            for r in remain:
                dist = abs(h[0]-r[0])+abs(h[1]-r[1])
                minDist = min(minDist, dist) # 지금 집이랑 남은 치킨집들 중 최소거리
            tmp += minDist # 도시의 치킨거리 += 제일 가까운 치킨집 거리
        res = min(res, tmp) # 이전 치킨거리랑 지금거랑 비교해서 작은게 답
print(res)