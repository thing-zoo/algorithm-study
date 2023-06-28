import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# 해당 노드의 부모를 저장하는 함수
def makeTree(node, p):
    for n in tree[node]: # 인접한 노드들
        if n != p:
            parent[n] = node # 자식 노드들의 부모를 자기자신으로 설정
            makeTree(n, node) 

# 해당 노드가 몇개의 서브트리를 가지고 있는지
def countSubTree(start):
    size[start] = 1 # 자기자신 1개
    for n in tree[start]:
        if not visited[n]:
            visited[n] = True
            countSubTree(n)
            size[start] += size[n] # 서브트리의 크기들을 더해줌

n, r, q = map(int, input().rstrip().split())
tree = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
size = [0]*(n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

makeTree(r, -1)
parent[r] = -1
visited[r] = True
countSubTree(r)
for _ in range(q):
    query = int(input())
    print(size[query])
