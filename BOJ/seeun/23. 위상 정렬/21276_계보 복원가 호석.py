import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
names = list(input().split())
nameTonum = {}
numToname = {}
i = 1

# 이름->번호, 번호->이름 각각 딕셔너리 만들어줌
for name in names:
    nameTonum[name] = i
    numToname[i] = name
    i += 1

# 트리 생성, 조상 인원수 카운트 ---------------------
m = int(input())
tree = [[] for _ in range(n+1)] # 자식들을 저장함
parent = [0]*(n+1) # i 사람의 조상 인원수
for _ in range(m):
    x, y = input().split()
    x, y = nameTonum[x], nameTonum[y]
    tree[y].append(x)
    parent[x] += 1

# 시조 찾기  -----------------------
root = []
queue = deque()
son = [[] for _ in range(n+1)] # 직계 자식 저장
for i in range(1, n+1):
    if parent[i] == 0: # 부모가 없는 노드들은 루트임
        root.append(numToname[i])

# 시조부터 내려오면서 탐색할거임 ----------------------
for r in root:
    queue.append(nameTonum[r]) 

while queue:
    per = queue.popleft()
    for i in tree[per]: # per의 자식들 탐색
        parent[i] -= 1 # 자식들의 조상인원수를 1 빼줌
        if parent[i] == 0: # 더이상 조상이 없으면 per의 아들이기 때문에 
            queue.append(i)
            son[per].append(numToname[i]) # 현재 사람의 자식 배열에 넣어줌

# 정답 출력 ---------------------
root.sort()
names.sort()
print(len(root))
print(" ".join(root))
for name in names:
    if len(son[nameTonum[name]]) == 0: # 리프노드이면
        print(name, 0)
    else:
        print(name, len(son[nameTonum[name]]), end=" ")
        son[nameTonum[name]].sort()
        for s in son[nameTonum[name]]:
            print(s, end=' ')
        print()
