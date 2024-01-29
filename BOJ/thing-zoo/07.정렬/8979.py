n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True) # 메달 수 기준 내림차순 정렬
idx = [medals[i][0] for i in range(n)].index(k) # 국가 k 인덱스 찾기
for i in range(n):
    if medals[i][1:] == medals[idx][1:]: # 동점국가 존재 여부 검사
        print(i+1) # 동점국가중 제일 첫번째 인덱스가 순위
        break