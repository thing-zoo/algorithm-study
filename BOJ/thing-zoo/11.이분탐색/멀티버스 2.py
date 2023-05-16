import bisect
m, n = map(int, input().split()) # 우주 m개, 행성 n개
universe = [list(map(int, input().split())) for _ in range(m)] # 우주별 행성 크기 배열

for uni in universe: # 좌표 압축
    temp = sorted(uni) # 정렬
    for i in range(len(uni)):
        uni[i] = bisect.bisect_left(temp, uni[i]) # lower_bound 찾기

answer = 0 # 균등한우주의 쌍의 개수
for i in range(m-1):
    for j in range(i+1, m):
        if universe[i] == universe[j]: # 균등한 우주쌍이면
            answer += 1 # 카운트
print(answer)