from collections import deque
def bfs(start):
    global cnt
    queue = deque()
    visited = [False] * n
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if tree[node]: # 자식 노드가 있으면
            for no in tree[node]:
                if not visited[no]:
                    visited[no] = True
                    queue.append(no)
        else: # 자식 노드가 없으면 리프노드 개수 +1
            cnt += 1

n = int(input())
parent = list(map(int, input().split()))
delete = int(input())

root = parent.index(-1) # 루트 노드 저장
parent[delete] = -99 # 지울 노드는 부모노드 없음
tree = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        continue
    if parent[i] == -99:
        continue
    tree[parent[i]].append(i)
tree[delete] = []

# print(tree)
cnt = 0
if delete == root: # 루트를 지우는 것이면 0 출력
    print(0)
else: # 아니면 bfs로 리프노드 개수 탐색
    bfs(root)
    print(cnt)