def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # 각각의 루트 노드 가져옴
    x = find(x) 
    y = find(y)

    if know[x] and know[y]: # 둘다 진실을 알고 있으면 합치지 않음
        return

    if know[x]: # x가 진실을 알고 있으면
        x, y = y, x # 두 값 스왑

    # x의 부모를 y로 지정
    parent[x] = y

n, m = map(int, input().split())
true_num = list(map(int, input().split())) # 진실을 알고 있는 사람 입력 받기
know = [False] * (n+1) # i사람이 진실을 알고 있는지 없는지
parent = [i for i in range(n+1)] # 초기 부모는 자기자신으로 설정
parties = [] # 파티 정보 입력 받기

if true_num == [0]: # 진실을 알고 있는 사람이 없으면 모든 파티에 과장 가능
    print(m)
    for _ in range(m):
        parties.append(list(map(int, input().split())))
else:
    true_num = true_num[1:]
    for i in range(len(true_num)): # 진실을 알고 있는 사람 True로 변경
        know[true_num[i]] = True

    # 같은 파티에 참석 하는 사람 끼리 유니온
    for _ in range(m):
        parties.append(list(map(int, input().split())))
        for i in range(1, len(parties[-1])-1):
            union(parties[-1][i], parties[-1][i+1])

    # 과장할 수 없는 파티 개수 세아리기  
    cant = 0
    for p in parties:
        flag = True
        for i in range(1, len(p)):
            root = find(p[i]) # 해당 파티원의 루트노드 가져오기
            if know[root]: # 진실을 아는 사람이면 현재 파티원도 진실을 앎
                cant += 1
                break

    # print(know)
    print(m-cant)