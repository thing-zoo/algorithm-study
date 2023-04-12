from itertools import combinations
def solution():
    answer = 1e9
    for selected in combinations(chickens, m): # m개의 치킨집 선택
        chicken_dists = 0 # 현재 도시의 치킨거리
        for x, y in houses: # 각 집 마다
            chicken_dist = 1e9
            for a, b in selected: # 치킨 거리 구하기
                dist = abs(x-a) + abs(y-b)
                chicken_dist = min(dist, chicken_dist)
            chicken_dists += chicken_dist
        answer = min(chicken_dists, answer)
    return answer

n, m = map(int, input().split())
grahp = []
houses = []
chickens = []
for i in range(n):
    grahp.append(list(map(int, input().split())))
    for j in range(n):
        if grahp[i][j] == 1:
            houses.append((i, j))
        elif grahp[i][j] == 2:
            chickens.append((i, j))
print(solution())