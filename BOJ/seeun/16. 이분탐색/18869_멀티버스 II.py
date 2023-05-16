from collections import defaultdict


m, n = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(m)]

spacezip = defaultdict(int)
for i in range(m):
    # 좌표압축
    spaceset = []
    spacedict = {}
    
    spaceset = set(space[i]) # 중복 제거
    spaceset = list(spaceset) # 리스트로 만들기
    spaceset.sort() # 오름차순 정렬
    
    # 행성을 오름차순으로 정렬해서 0부터 번호를 매김
    for j in range(len(spaceset)):
        spacedict[spaceset[j]] = j

    # 현재 우주를 압축된 번호로 표현하기
    tmp = []
    for j in range(n):
        tmp.append(spacedict[space[i][j]])
    
    # 딕셔너리에서 압축된 번호로 표현한 행성이 몇개 있는지 카운트
    spacezip[tuple(tmp)] += 1


cnt = 0
for i in spacezip.values():
    cnt += i * (i-1) // 2

print(cnt)